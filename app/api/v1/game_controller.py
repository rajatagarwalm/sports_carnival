from fastapi import APIRouter, HTTPException
from app.schemas.game_schema import GameCreate, GameOut, GameUpdate
from app.services import game_service
from typing import List

router = APIRouter()

@router.post("/carnivals/{carnival_id}/games/", response_model=GameOut)
def create_game(carnival_id: str, payload: GameCreate):
    result = game_service.create_game(carnival_id, payload)
    if not result:
        raise HTTPException(status_code=400, detail="Game already exists")
    return result

@router.get("/carnivals/{carnival_id}/games/", response_model=List[GameOut])
def list_games(carnival_id: str):
    return game_service.list_games(carnival_id)

@router.get("/carnivals/{carnival_id}/games/{game_id}", response_model=GameOut)
def get_game(carnival_id: str, game_id: str):
    result = game_service.get_game(carnival_id, game_id)
    if not result:
        raise HTTPException(status_code=404, detail="Game not found")
    return result

@router.put("/carnivals/{carnival_id}/games/{game_id}", response_model=GameOut)
def update_game(carnival_id: str, game_id: str, payload: GameUpdate):
    result = game_service.update_game(carnival_id, game_id, payload)
    if not result:
        raise HTTPException(status_code=404, detail="Game not found or new game_id already exists")
    return result

@router.delete("/carnivals/{carnival_id}/games/{game_id}", response_model=dict)
def delete_game(carnival_id: str, game_id: str):
    success = game_service.delete_game(carnival_id, game_id)
    if not success:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": "Game deleted successfully"}
