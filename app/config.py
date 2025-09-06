import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Student Portal API"

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./student_portal.db")

    # JWT / Security
    JWT_SECRET: str = os.getenv("SECRET_KEY", "supersecret")
    JWT_ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    JWT_EXPIRES_IN: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)) * 60  # seconds

settings = Settings()
