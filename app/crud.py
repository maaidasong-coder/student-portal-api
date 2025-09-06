from sqlalchemy.orm import Session
from app import models
from app.schemas import UserCreate
from passlib.hash import bcrypt


# ===============================
# USER CRUD
# ===============================

def create_user(db: Session, user: UserCreate):
    """Create a new user with hashed password"""
    hashed_pw = bcrypt.hash(user.password)
    db_user = models.User(
        email=user.email,
        password_hash=hashed_pw,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    """Fetch a user by email"""
    return db.query(models.User).filter(models.User.email == email).first()


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plain password against its hashed version"""
    return bcrypt.verify(plain, hashed)


# ===============================
# STUDENT CRUD (optional, extend later)
# ===============================

def create_student(db: Session, user_id: int, matric_no: str, name: str, program: str, level: str, session: str):
    """Create a student linked to an existing user"""
    student = models.Student(
        user_id=user_id,
        matric_no=matric_no,
        name=name,
        program=program,
        level=level,
        session=session
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student_by_matric(db: Session, matric_no: str):
    """Fetch student by matric number"""
    return db.query(models.Student).filter(models.Student.matric_no == matric_no).first()
