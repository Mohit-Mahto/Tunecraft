from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
import numpy as np
import tempfile
import os
from auth import get_current_user
import models

router = APIRouter(prefix="/api/analyze", tags=["analyze"])

@router.post("/track")
async def analyze_track(
    file: UploadFile = File(...),
    current_user: models.User = Depends(get_current_user)
):
    try:
        import librosa

        # Save uploaded file to temp
        suffix = ".mp3" if file.filename.endswith(".mp3") else ".wav"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Load audio
        y, sr = librosa.load(tmp_path, duration=60, mono=True)
        os.unlink(tmp_path)

        # --- BPM Detection ---
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        bpm = round(float(np.atleast_1d(tempo)[0]), 1)

        # --- Waveform (downsample to 300 points) ---
        step = max(1, len(y) // 300)
        waveform = [round(float(x), 4) for x in y[::step][:300]]

        # --- Frequency Analysis ---
        stft = np.abs(librosa.stft(y))
        freqs = librosa.fft_frequencies(sr=sr)

        # Bass: 20-250 Hz
        bass_mask = (freqs >= 20) & (freqs <= 250)
        bass_energy = float(np.mean(stft[bass_mask]))

        # Mid: 250-4000 Hz
        mid_mask = (freqs >= 250) & (freqs <= 4000)
        mid_energy = float(np.mean(stft[mid_mask]))

        # Treble: 4000-20000 Hz
        treble_mask = (freqs >= 4000) & (freqs <= 20000)
        treble_energy = float(np.mean(stft[treble_mask]))

        # Normalize to percentages
        total = bass_energy + mid_energy + treble_energy
        bass_pct = round(bass_energy / total * 100, 1)
        mid_pct = round(mid_energy / total * 100, 1)
        treble_pct = round(treble_energy / total * 100, 1)

        # --- Harmonic vs Percussive separation ---
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        harmonic_energy = float(np.mean(np.abs(y_harmonic)))
        percussive_energy = float(np.mean(np.abs(y_percussive)))
        total_hp = harmonic_energy + percussive_energy
        harmonic_pct = round(harmonic_energy / total_hp * 100, 1)
        percussive_pct = round(percussive_energy / total_hp * 100, 1)

        # --- Spectral features ---
        spectral_centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
        zcr = float(np.mean(librosa.feature.zero_crossing_rate(y)))

        # --- Energy/loudness over time (for drop detection) ---
        rms = librosa.feature.rms(y=y)[0]
        rms_normalized = [round(float(x), 4) for x in rms[::max(1, len(rms)//100)][:100]]

        # --- Duration ---
        duration = round(len(y) / sr, 1)

        # --- Beginner tips ---
        tips = []
        if bass_pct > 45:
            tips.append("🔊 This track is very bass-heavy. The low-end dominates the mix — great for Hip Hop or EDM.")
        elif bass_pct < 20:
            tips.append("🎵 Light on bass. This track relies more on melody and highs — common in pop or acoustic music.")
        else:
            tips.append("⚖️ Well-balanced bass. The low-end supports without overpowering.")

        if bpm < 90:
            tips.append("🐢 Slow tempo (under 90 BPM). Great for ballads, R&B, or chill music.")
        elif bpm < 130:
            tips.append("🚶 Medium tempo (90-130 BPM). Perfect for Hip Hop, Pop, and most mainstream music.")
        else:
            tips.append("⚡ Fast tempo (over 130 BPM). This is EDM/Dance territory — high energy!")

        if percussive_pct > 55:
            tips.append("🥁 Strong percussive presence. The drums and rhythm are the backbone of this track.")
        else:
            tips.append("🎹 Melody-driven track. The harmonic elements (chords, melody) carry this song.")

        if treble_pct > 40:
            tips.append("✨ Bright and airy sound. High frequencies are prominent — great for clarity.")

        return {
            "success": True,
            "filename": file.filename,
            "duration": duration,
            "bpm": bpm,
            "waveform": waveform,
            "rms_energy": rms_normalized,
            "frequency": {
                "bass": bass_pct,
                "mid": mid_pct,
                "treble": treble_pct
            },
            "elements": {
                "harmonic": harmonic_pct,
                "percussive": percussive_pct
            },
            "spectral_centroid": round(spectral_centroid, 1),
            "tips": tips
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})
