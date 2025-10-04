from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import GptResponse, User, Course, Lesson, Material, Book
from schemas import GptResponses, UserCreate, UserResponse, CourseResponse, LessonResponse, MaterialResponse, BookResponse, AnswerRequest, AnswerResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from database import database, metadata, engine
from typing import List
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.openai_helpers import chat_helper
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
class ChatInput(BaseModel): #what user inputs
    userMessage: str

# Existing routes
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": db_user.username, "token_type": "bearer"}

#Gpt Responses
@router.get("/responses", response_model=list[GptResponses])
def get_courses(db: Session = Depends(get_db)):
    return db.query(GptResponse).all()

@router.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(Course).all()

@router.get("/courses/{course_id}/lessons", response_model=list[LessonResponse])
def get_lessons(course_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(Lesson).filter(Lesson.course_id == course_id).all()

@router.get("/courses/{course_id}/materials", response_model=list[MaterialResponse])
def get_materials(course_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(Material).filter(Material.course_id == course_id).all()

@router.get("/courses/{course_id}/books", response_model=list[BookResponse])
def get_books(course_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(Book).filter(Book.course_id == course_id).all()

@router.get("/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.post("/lessons/{lesson_id}/answer", response_model=AnswerResponse)
async def submit_answer(lesson_id: int, answer: AnswerRequest, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    logger.debug(f"/lessons/{lesson_id}/answer - Received input: {answer.content}")
    message = {"role": "user", "content": answer.content}
    try:
        result = await chat_helper(message)
        logger.debug(f"/lessons/{lesson_id}/answer - Returning result: {result}")
        final_result = result.get("content") if isinstance(result,dict) else str(result)
        db_message = GptResponse(text = f"{final_result}")
        db.add(db_message)
        db.commit() 
        db.refresh(db_message)
        return {"response": f"{final_result}"}
    except Exception as e:
        logger.error(f"/sendText - Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# New endpoints for individual materials and books
@router.get("/materials/{material_id}", response_model=MaterialResponse)
def get_material(material_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

@router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Seed endpoint (if you added it previously)
@router.post("/seed")
def seed_database(db: Session = Depends(get_db)):
    if db.query(Course).count() > 0:
        raise HTTPException(status_code=400, detail="Database already seeded")
    courses = [
        Course(id=1, name="1st Course"),
        Course(id=2, name="Olympiad Preparation"),
        Course(id=3, name="3rd Course")
    ]
    db.add_all(courses)
    lessons = [
        Lesson(course_id=1, title="Lesson 1", pdf_url="http://example.com/pdf1.pdf", video_url="http://example.com/video1.mp4", transcript="Transcript 1..."),
        Lesson(course_id=1, title="Lesson 2", video_url="http://example.com/video2.mp4", transcript="Transcript 2..."),
        Lesson(course_id=1, title="Lesson 3", pdf_url="http://example.com/pdf3.pdf", transcript="Transcript 3..."),
        Lesson(course_id=1, title="Lesson 4", pdf_url="http://example.com/pdf4.pdf", transcript="Transcript 4..."),
        Lesson(course_id=1, title="Lesson 5", video_url="http://example.com/video5.mp4", transcript="Transcript 5..."),
        Lesson(course_id=1, title="Lesson 6", pdf_url="http://example.com/pdf6.pdf", transcript="Transcript 6...")
    ]
    db.add_all(lessons)
    materials = [
        Material(course_id=2, title="Material 1", pdf_url="http://example.com/material1.pdf"),
        Material(course_id=2, title="Material 2", pdf_url="http://example.com/material2.pdf")
    ]
    db.add_all(materials)
    books = [
        Book(course_id=3, title="Book 1", pdf_url="http://example.com/book1.pdf"),
        Book(course_id=3, title="Book 2", pdf_url="http://example.com/book2.pdf")
    ]
    db.add_all(books)
    db.commit()
    return {"message": "Database seeded successfully"}