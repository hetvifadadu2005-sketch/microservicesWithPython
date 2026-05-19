from fastapi import APIRouter

router = APIRouter(prefix="/v1/games")

games = []

@router.get("/health")
def health():
    return {"status": "game service running"}