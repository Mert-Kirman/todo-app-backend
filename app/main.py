from fastapi import FastAPI
from app.db import create_tables
from app.models import User, Todo  # Import models so SQLAlchemy registers them

create_tables()

app = FastAPI()

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}