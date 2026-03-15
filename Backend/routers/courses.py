from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from database import get_db
import models
from auth import get_current_user

router = APIRouter(prefix="/api/courses", tags=["courses"])


# --- Schemas ---
class LessonOut(BaseModel):
    id: int
    title: str
    title_hi: Optional[str] = None
    description: Optional[str] = None
    description_hi: Optional[str] = None
    video_url: Optional[str] = None
    order: int
    duration_minutes: int

    class Config:
        orm_mode = True

class CourseOut(BaseModel):
    id: int
    title: str
    title_hi: Optional[str] = None
    description: Optional[str] = None
    description_hi: Optional[str] = None
    order: int
    lessons: List[LessonOut] = []

    class Config:
        orm_mode = True


# --- Routes ---
@router.get("/", response_model=List[CourseOut])
def get_courses(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Course).order_by(models.Course.order).all()


@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.get("/{course_id}/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(course_id: int, lesson_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    lesson = db.query(models.Lesson).filter(
        models.Lesson.id == lesson_id,
        models.Lesson.course_id == course_id
    ).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson
