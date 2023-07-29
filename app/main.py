from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import api
from .core.database import engine
from .models import user, post

user.Base.metadata.create_all(bind=engine)
post.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
