from fastapi import FastAPI
from app.db import create_tables
from app.models import User, Todo  # Import models so SQLAlchemy registers them
from app.api import todos, users

create_tables()

app = FastAPI()

app.include_router(users.router)
app.include_router(todos.router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}