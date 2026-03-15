from database import SessionLocal
import models

def seed_data():
    db = SessionLocal()
    try:
        if db.query(models.Course).count() > 0:
            return

        courses_data = [
            {
                "title": "Music Production Basics",
                "title_hi": "म्यूजिक प्रोडक्शन की बेसिक्स",
                "description": "Learn the fundamental concepts of music production from scratch.",
                "description_hi": "संगीत उत्पादन की बुनियादी अवधारणाएं सीखें।",
                "order": 1,
                "lessons": [
                    {"title": "What is Music Production?", "title_hi": "म्यूजिक प्रोडक्शन क्या है?", "description": "An introduction to music production and what producers do.", "description_hi": "म्यूजिक प्रोडक्शन का परिचय।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 10},
                    {"title": "Understanding DAWs", "title_hi": "DAW को समझें", "description": "What is a Digital Audio Workstation and which one to choose.", "description_hi": "डिजिटल ऑडियो वर्कस्टेशन क्या है।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 12},
                    {"title": "Beats, BPM & Rhythm", "title_hi": "बीट्स, BPM और ताल", "description": "Understanding tempo, beats per minute, and basic rhythm.", "description_hi": "टेम्पो और BPM को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 15},
                    {"title": "Setting Up Your Studio", "title_hi": "अपना स्टूडियो सेट करें", "description": "How to set up a basic home studio for music production.", "description_hi": "होम स्टूडियो कैसे सेट करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 18},
                ]
            },
            {
                "title": "Mixing Fundamentals",
                "title_hi": "मिक्सिंग की बुनियादी बातें",
                "description": "Learn how to mix tracks like a professional.",
                "description_hi": "प्रोफेशनल की तरह ट्रैक मिक्स करना सीखें।",
                "order": 2,
                "lessons": [
                    {"title": "What is Mixing?", "title_hi": "मिक्सिंग क्या है?", "description": "Introduction to audio mixing and why it matters.", "description_hi": "ऑडियो मिक्सिंग का परिचय।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 10},
                    {"title": "EQ Explained", "title_hi": "EQ की जानकारी", "description": "Understanding equalization and how to use it.", "description_hi": "इक्वलाइज़ेशन को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 18},
                    {"title": "Compression Basics", "title_hi": "कंप्रेशन की बेसिक्स", "description": "What compression does and when to use it.", "description_hi": "कंप्रेशन क्या करता है।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 20},
                    {"title": "Reverb & Delay", "title_hi": "रिवर्ब और डिले", "description": "Adding space and depth to your mix with reverb and delay.", "description_hi": "रिवर्ब और डिले से मिक्स में गहराई जोड़ें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 16},
                ]
            },
            {
                "title": "Sound Design",
                "title_hi": "साउंड डिज़ाइन",
                "description": "Create your own unique sounds and synth patches.",
                "description_hi": "अपनी खुद की आवाज़ें और सिंथ पैच बनाएं।",
                "order": 3,
                "lessons": [
                    {"title": "Intro to Synthesizers", "title_hi": "सिंथेसाइज़र का परिचय", "description": "How synthesizers work and basic sound design.", "description_hi": "सिंथेसाइज़र कैसे काम करते हैं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 22},
                    {"title": "Oscillators & Waveforms", "title_hi": "ऑसिलेटर और वेवफॉर्म", "description": "Understanding oscillators, sine, square, sawtooth waves.", "description_hi": "ऑसिलेटर और वेवफॉर्म को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 18},
                    {"title": "Filters & Envelopes", "title_hi": "फ़िल्टर और एनवेलप", "description": "Shaping your sound with filters and ADSR envelopes.", "description_hi": "फ़िल्टर और ADSR से आवाज़ बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 20},
                ]
            },
            {
                "title": "Beat Making",
                "title_hi": "बीट मेकिंग",
                "description": "Learn how to create hard-hitting beats from scratch.",
                "description_hi": "स्क्रैच से धमाकेदार बीट्स बनाना सीखें।",
                "order": 4,
                "lessons": [
                    {"title": "Drum Patterns 101", "title_hi": "ड्रम पैटर्न 101", "description": "Creating your first drum pattern with kick, snare and hi-hat.", "description_hi": "किक, स्नेयर और हाई-हैट से पहला ड्रम पैटर्न बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 20},
                    {"title": "Layering Drums", "title_hi": "ड्रम लेयरिंग", "description": "How to layer drum sounds for a fuller, punchier beat.", "description_hi": "ड्रम साउंड लेयर करके बीट को पंची बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 18},
                    {"title": "Adding Melody to Beats", "title_hi": "बीट्स में मेलोडी जोड़ें", "description": "How to add melodic elements on top of your drum pattern.", "description_hi": "ड्रम पैटर्न के ऊपर मेलोडी कैसे जोड़ें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 22},
                    {"title": "Beat Arrangement", "title_hi": "बीट अरेंजमेंट", "description": "Arranging your beat into a full track structure.", "description_hi": "बीट को पूरे ट्रैक में कैसे अरेंज करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 25},
                ]
            },
            {
                "title": "Music Theory for Producers",
                "title_hi": "प्रोड्यूसर्स के लिए म्यूजिक थ्योरी",
                "description": "Essential music theory every producer needs to know.",
                "description_hi": "हर प्रोड्यूसर को जरूरी म्यूजिक थ्योरी।",
                "order": 5,
                "lessons": [
                    {"title": "Notes, Scales & Keys", "title_hi": "नोट्स, स्केल्स और की", "description": "Understanding musical notes, scales and keys.", "description_hi": "म्यूजिकल नोट्स, स्केल्स और की को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 20},
                    {"title": "Chords & Progressions", "title_hi": "कॉर्ड्स और प्रोग्रेशन", "description": "Building chords and creating chord progressions.", "description_hi": "कॉर्ड्स बनाना और कॉर्ड प्रोग्रेशन।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 25},
                    {"title": "Melody Writing", "title_hi": "मेलोडी लिखना", "description": "How to write catchy and memorable melodies.", "description_hi": "यादगार मेलोडी कैसे लिखें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 22},
                    {"title": "Song Structure", "title_hi": "सॉन्ग स्ट्रक्चर", "description": "Verse, chorus, bridge — how songs are structured.", "description_hi": "वर्स, कोरस, ब्रिज — गाने की संरचना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 18},
                ]
            },
            {
                "title": "Sampling & Loops",
                "title_hi": "सैंपलिंग और लूप्स",
                "description": "Master the art of sampling and creating loops.",
                "description_hi": "सैंपलिंग और लूप्स की कला सीखें।",
                "order": 6,
                "lessons": [
                    {"title": "What is Sampling?", "title_hi": "सैंपलिंग क्या है?", "description": "The history and art of sampling in music production.", "description_hi": "म्यूजिक प्रोडक्शन में सैंपलिंग का इतिहास।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 15},
                    {"title": "Chopping Samples", "title_hi": "सैंपल्स चॉप करना", "description": "How to chop and rearrange audio samples creatively.", "description_hi": "ऑडियो सैंपल्स को क्रिएटिव तरीके से चॉप करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 20},
                    {"title": "Creating Loop Packs", "title_hi": "लूप पैक बनाना", "description": "How to create your own loop packs and samples.", "description_hi": "अपने खुद के लूप पैक कैसे बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 18},
                ]
            },
            {
                "title": "Recording Vocals",
                "title_hi": "वोकल रिकॉर्डिंग",
                "description": "Learn how to record, edit and process vocals professionally.",
                "description_hi": "वोकल प्रोफेशनल तरीके से रिकॉर्ड करना सीखें।",
                "order": 7,
                "lessons": [
                    {"title": "Microphone Basics", "title_hi": "माइक्रोफोन की बेसिक्स", "description": "Types of microphones and how to choose the right one.", "description_hi": "माइक्रोफोन के प्रकार और सही माइक कैसे चुनें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 15},
                    {"title": "Recording Techniques", "title_hi": "रिकॉर्डिंग तकनीक", "description": "Best practices for recording clean, professional vocals.", "description_hi": "क्लीन वोकल रिकॉर्ड करने के सबसे अच्छे तरीके।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 20},
                    {"title": "Vocal Processing", "title_hi": "वोकल प्रोसेसिंग", "description": "EQ, compression and effects for professional sounding vocals.", "description_hi": "वोकल को प्रोफेशनल साउंड देने के लिए EQ और कंप्रेशन।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 22},
                    {"title": "Vocal Tuning & Editing", "title_hi": "वोकल ट्यूनिंग और एडिटिंग", "description": "How to tune and edit vocals for a polished result.", "description_hi": "वोकल ट्यून और एडिट कैसे करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 18},
                ]
            },
            {
                "title": "Mastering",
                "title_hi": "मास्टरिंग",
                "description": "The final step — master your tracks for release.",
                "description_hi": "अंतिम चरण — रिलीज के लिए अपने ट्रैक को मास्टर करें।",
                "order": 8,
                "lessons": [
                    {"title": "What is Mastering?", "title_hi": "मास्टरिंग क्या है?", "description": "Understanding the mastering process and why it matters.", "description_hi": "मास्टरिंग प्रक्रिया को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 12},
                    {"title": "Loudness & Dynamics", "title_hi": "लाउडनेस और डायनामिक्स", "description": "Understanding LUFS, loudness standards and dynamic range.", "description_hi": "LUFS और लाउडनेस स्टैंडर्ड को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 18},
                    {"title": "Mastering Chain", "title_hi": "मास्टरिंग चेन", "description": "Building a mastering chain: EQ, compression, limiting.", "description_hi": "मास्टरिंग चेन बनाना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 25},
                    {"title": "Exporting Your Track", "title_hi": "ट्रैक एक्सपोर्ट करना", "description": "Exporting settings for Spotify, YouTube and other platforms.", "description_hi": "Spotify और YouTube के लिए ट्रैक एक्सपोर्ट करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 14},
                ]
            },
            {
                "title": "Hip Hop Production",
                "title_hi": "हिप हॉप प्रोडक्शन",
                "description": "Learn to produce hard-hitting Hip Hop tracks.",
                "description_hi": "धमाकेदार हिप हॉप ट्रैक बनाना सीखें।",
                "order": 9,
                "lessons": [
                    {"title": "Hip Hop Beat Structure", "title_hi": "हिप हॉप बीट स्ट्रक्चर", "description": "Understanding the anatomy of a Hip Hop beat.", "description_hi": "हिप हॉप बीट की संरचना को समझना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 18},
                    {"title": "808s & Trap Drums", "title_hi": "808 और ट्रैप ड्रम्स", "description": "Working with 808 bass and trap drum patterns.", "description_hi": "808 बेस और ट्रैप ड्रम पैटर्न के साथ काम करना।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 22},
                    {"title": "Sampling for Hip Hop", "title_hi": "हिप हॉप के लिए सैंपलिंग", "description": "How classic Hip Hop producers sample and flip records.", "description_hi": "क्लासिक हिप हॉप प्रोड्यूसर कैसे सैंपल करते हैं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 20},
                ]
            },
            {
                "title": "EDM & Electronic Music",
                "title_hi": "EDM और इलेक्ट्रॉनिक म्यूजिक",
                "description": "Create club-ready EDM tracks and electronic music.",
                "description_hi": "क्लब-रेडी EDM ट्रैक और इलेक्ट्रॉनिक म्यूजिक बनाएं।",
                "order": 10,
                "lessons": [
                    {"title": "EDM Song Structure", "title_hi": "EDM सॉन्ग स्ट्रक्चर", "description": "Drop, build-up, breakdown — EDM arrangement explained.", "description_hi": "ड्रॉप, बिल्ड-अप, ब्रेकडाउन — EDM अरेंजमेंट।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 1, "duration_minutes": 20},
                    {"title": "Synth Leads & Pads", "title_hi": "सिंथ लीड्स और पैड्स", "description": "Designing classic EDM synth leads and atmospheric pads.", "description_hi": "EDM सिंथ लीड्स और पैड्स डिज़ाइन करें।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 2, "duration_minutes": 24},
                    {"title": "The Drop", "title_hi": "द ड्रॉप", "description": "How to build and design an impactful EDM drop.", "description_hi": "इम्पैक्टफुल EDM ड्रॉप कैसे बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 3, "duration_minutes": 28},
                    {"title": "Sidechain Compression", "title_hi": "साइडचेन कंप्रेशन", "description": "The pumping EDM effect using sidechain compression.", "description_hi": "साइडचेन कंप्रेशन से EDM पंपिंग इफेक्ट बनाएं।", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "order": 4, "duration_minutes": 20},
                ]
            },
        ]

        for course_data in courses_data:
            lessons_data = course_data.pop("lessons")
            course = models.Course(**course_data)
            db.add(course)
            db.flush()
            for lesson_data in lessons_data:
                lesson = models.Lesson(course_id=course.id, **lesson_data)
                db.add(lesson)

        db.commit()
        print("✅ Seed data loaded — 10 courses ready!")

    except Exception as e:
        db.rollback()
        print(f"⚠️ Seed error: {e}")
    finally:
        db.close()
