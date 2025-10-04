from pydantic import BaseModel
from typing import Optional, List

class GptResponses(BaseModel):
    text: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class LessonResponse(BaseModel):
    id: int
    title: str
    pdf_lesson: Optional[str]
    pdf_url: Optional[str]
    pdf_url1: Optional[str]
    pdf_answers: Optional[str]
    video_url: Optional[str]
    transcript: Optional[str]
    class Config:
        from_attributes = True

class MaterialResponse(BaseModel):
    id: int
    title: str
    pdf_url: str
    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    id: int
    title: str
    pdf_url: str
    class Config:
        from_attributes = True

class CourseResponse(BaseModel):
    id: int
    name: str
    lessons: List[LessonResponse] = []
    materials: List[MaterialResponse] = []
    books: List[BookResponse] = []
    class Config:
        from_attributes = True

class AnswerRequest(BaseModel):
    content: str

class AnswerResponse(BaseModel):
    response: str