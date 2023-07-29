from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
def main():
    return {"message": "Hello World"}
