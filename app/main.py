from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, students
from app.database import engine, Base

# ===============================
# DATABASE SETUP
# ===============================
# Auto-create tables in development (use Alembic for production migrations)
Base.metadata.create_all(bind=engine)

# ===============================
# APP INIT
# ===============================
app = FastAPI(
    title="STC Student Portal API",
    version="1.0.0",
    description="Backend API for managing students, users, and authentication in the student portal."
)

# ===============================
# CORS SETUP
# ===============================
origins = [
    "http://localhost:3000",  # local dev frontend
    "https://your-frontend-app.vercel.app",  # replace with your deployed frontend
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
# Authentication endpoints
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Student endpoints
app.include_router(students.router, prefix="/students", tags=["Students"])
