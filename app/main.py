from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, students
from app.database import engine, Base


# ===============================
# DATABASE SETUP
# ===============================
# For dev: auto-create tables (in production, use Alembic migrations)
Base.metadata.create_all(bind=engine)


# ===============================
# APP INIT
# ===============================
app = FastAPI(
    title="Student Portal API",
    version="1.0.0",
    description="Backend API for managing students, users, and authentication in the student portal."
)


# ===============================
# CORS SETUP
# ===============================
# Allow frontend apps (e.g., Vercel) to call this API
origins = [
    "http://localhost:3000",  # local dev frontend
    "https://your-frontend-app.vercel.app",  # replace with actual Vercel domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===============================
# ROUTES
# ===============================
@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


# Register route modules
app.include_router(auth.router)
app.include_router(students.router)
