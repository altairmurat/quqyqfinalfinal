from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class GptResponse(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # In production, use hashed passwords
    lessons = relationship("Lesson", secondary="user_lessons")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lessons = relationship("Lesson", back_populates="course")
    materials = relationship("Material", back_populates="course")
    books = relationship("Book", back_populates="course")

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    pdf_lesson = Column(String, nullable=True)
    pdf_url = Column(String, nullable=True)
    pdf_url1 = Column(String, nullable=True)
    pdf_answers = Column(String, nullable=True)
    video_url = Column(String, nullable=True)
    transcript = Column(Text, nullable=True)
    course = relationship("Course", back_populates="lessons")

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    pdf_url = Column(String)
    course = relationship("Course", back_populates="materials")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    pdf_url = Column(String)
    course = relationship("Course", back_populates="books")

class UserLesson(Base):  # Junction table for user-lesson progress
    __tablename__ = "user_lessons"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), primary_key=True)