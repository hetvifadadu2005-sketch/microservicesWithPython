from fastapi import APIRouter

router = APIRouter(prefix="/v1/games")

# fake in-memory DB
games = []

@router.post("/")
def create_game(game: dict):
    games.append(game)
    return game

@router.get("/")
def list_games(limit: int = 10, offset: int = 0):
    return games[offset: offset + limit]

@router.get("/search")
def search_games(q: str):
    return [g for g in games if q.lower() in g.get("title", "").lower()]

@router.get("/{game_id}")
def get_game(game_id: int):
    if game_id >= len(games):
        return {"error": "not found"}
    return games[game_id]