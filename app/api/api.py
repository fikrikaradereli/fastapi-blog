from fastapi import APIRouter

from . import root, auth, users, posts

router = APIRouter()

router.include_router(root.router)
router.include_router(auth.router)
router.include_router(users.router)
router.include_router(posts.router)
