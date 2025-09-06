from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, students
from app.database import engine, Base

# ===============================
# DATABASE SETUP
# ===============================
# For development: auto-create tables (in production, use Alembic migrations)
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
origins = [
    "http://localhost:3000",  # local dev frontend
    "https://your-frontend-app.vercel.app",  # replace with actual frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# ROOT & HEALTH ENDPOINTS
# ===============================
@app.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {"message": "STC Student Portal API is live!"}


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

# ===============================
# ROUTES
# ===============================
# Auth routes with /auth prefix
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Student routes with /students prefix
app.include_router(students.router, prefix="/students", tags=["Students"])
