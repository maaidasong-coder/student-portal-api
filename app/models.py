from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime


# ===============================
# USER MODEL
# ===============================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="student")  # roles: "student", "admin"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # One-to-One relationship with Student
    student = relationship("Student", back_populates="user", uselist=False)


# ===============================
# STUDENT MODEL
# ===============================

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    matric_no = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    program = Column(String, nullable=True)
    level = Column(String, nullable=True)
    session = Column(String, nullable=True)

    # Back reference to User
    user = relationship("User", back_populates="student")
