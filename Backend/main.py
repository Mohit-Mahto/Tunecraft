# Python 3.13 + pydantic v1 compatibility patch — MUST be first
import sys
import typing
if sys.version_info >= (3, 12):
    _orig = typing.ForwardRef._evaluate
    def _patched(self, globalns, localns, *args, **kwargs):
        kwargs.setdefault('recursive_guard', frozenset())
        return _orig(self, globalns, localns, **kwargs)
    typing.ForwardRef._evaluate = _patched

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import users, courses, progress
from seed import seed_data

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tunecraft API", version="1.0.0")

# CORS — allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(progress.router)


@app.get("/")
def root():
    return {"message": "Welcome to Tunecraft API 🎵"}


@app.on_event("startup")
def on_startup():
    seed_data()
