from typing import Annotated
from fastapi import APIRouter, Depends
from app import schemas, crud
from app.core.database import SessionLocal
from .dependencies import get_current_user, get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.post("/", response_model=schemas.Post)
def create_post(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
    post: schemas.PostCreate,
):
    return crud.post.create_post(db, post)


@router.get("/", response_model=list[schemas.Post])
def read_posts(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
):
    return crud.post.get_posts(db)


@router.get("/{post_id}", response_model=schemas.Post)
def read_post(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
    post_id: int,
):
    return crud.post.get_post(db, post_id)


@router.get("/user/{user_id}", response_model=list[schemas.Post])
def read_user_posts(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
    user_id: int,
):
    return crud.post.get_user_posts(db, user_id)
