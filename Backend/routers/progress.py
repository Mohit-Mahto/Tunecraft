from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import List
from datetime import datetime
from database import get_db
import models
from auth import get_current_user

router = APIRouter(prefix="/api/progress", tags=["progress"])


# --- Schemas ---
class MarkComplete(BaseModel):
    lesson_id: int

class QuizAnswer(BaseModel):
    quiz_id: int
    selected_option: str  # "a", "b", "c", or "d"

class ProgressSummary(BaseModel):
    total_lessons: int
    completed_lessons: int
    percentage: float


# --- Routes ---
@router.post("/complete")
def mark_lesson_complete(data: MarkComplete, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    existing = db.query(models.UserProgress).filter_by(
        user_id=current_user.id, lesson_id=data.lesson_id
    ).first()

    if existing:
        existing.completed = True
        existing.completed_at = datetime.utcnow()
    else:
        progress = models.UserProgress(
            user_id=current_user.id,
            lesson_id=data.lesson_id,
            completed=True,
            completed_at=datetime.utcnow()
        )
        db.add(progress)

    db.commit()
    return {"message": "Lesson marked as complete"}


@router.get("/summary", response_model=ProgressSummary)
def get_progress_summary(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    total = db.query(models.Lesson).count()
    completed = db.query(models.UserProgress).filter_by(
        user_id=current_user.id, completed=True
    ).count()
    percentage = round((completed / total * 100), 1) if total > 0 else 0.0
    return {"total_lessons": total, "completed_lessons": completed, "percentage": percentage}


@router.post("/quiz")
def submit_quiz(data: QuizAnswer, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == data.quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    is_correct = data.selected_option.lower() == quiz.correct_option.lower()
    result = models.QuizResult(
        user_id=current_user.id,
        quiz_id=data.quiz_id,
        selected_option=data.selected_option,
        is_correct=is_correct
    )
    db.add(result)
    db.commit()
    return {"is_correct": is_correct, "correct_option": quiz.correct_option}
