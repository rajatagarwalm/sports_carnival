from fastapi import APIRouter, HTTPException
from app.schemas.game_schema import GameCreate, GameOut, GameUpdate
from app.services import game_service
from typing import List

router = APIRouter()

@router.post("/carnivals/{carnival_id}/games/", response_model=GameOut)
def create_game(carnival_id: str, payload: GameCreate):
    try:
        result = game_service.create_game(carnival_id, payload)
        if not result:
            raise HTTPException(status_code=400, detail="Game already exists")
        return result
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/carnivals/{carnival_id}/games/", response_model=List[GameOut])
def list_games(carnival_id: str):
    try:
        return game_service.list_games(carnival_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/carnivals/{carnival_id}/games/{game_id}", response_model=GameOut)
def get_game(carnival_id: str, game_id: str):
    try:
        result = game_service.get_game(carnival_id, game_id)
        if not result:
            raise HTTPException(status_code=404, detail="Game not found")
        return result
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/carnivals/{carnival_id}/games/{game_id}", response_model=GameOut)
def update_game(carnival_id: str, game_id: str, payload: GameUpdate):
    try:
        result = game_service.update_game(carnival_id, game_id, payload)
        if not result:
            raise HTTPException(status_code=404, detail="Game not found or new game_id already exists")
        return result
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.delete("/carnivals/{carnival_id}/games/{game_id}", response_model=dict)
def delete_game(carnival_id: str, game_id: str):
    try:
        success = game_service.delete_game(carnival_id, game_id)
        if not success:
            raise HTTPException(status_code=404, detail="Game not found")
        return {"message": "Game deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
