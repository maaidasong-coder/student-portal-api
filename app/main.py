from fastapi import FastAPI
from app.routes import auth, students
from app.database import engine, Base

# Create tables automatically (Alembic later for real migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Portal API", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(students.router, prefix="/students", tags=["Students"])
