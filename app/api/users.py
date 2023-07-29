from typing import Annotated
from fastapi import APIRouter, Depends
from app import schemas, crud
from app.core.database import SessionLocal
from .dependencies import get_current_user, get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[schemas.User])
def read_users(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
):
    return crud.user.get_users(db)


@router.get("/me", response_model=schemas.User)
def read_user_me(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    db: Annotated[SessionLocal, Depends(get_db)],
    current_user: Annotated[schemas.User, Depends(get_current_user)],
    user_id: int,
):
    return crud.user.get_user_by_id(db, user_id)
