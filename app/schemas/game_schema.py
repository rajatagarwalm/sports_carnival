from pydantic import BaseModel
from typing import List, Optional

class GameCreate(BaseModel):
    game_id: str
    name: str
    categories: List[str]

class GameUpdate(BaseModel):
    new_game_id: Optional[str]
    name: Optional[str]
    categories: Optional[List[str]]

class GameOut(BaseModel):
    carnival_id: str
    game_id: str
    name: str
    categories: List[str]
    created_at: str
    updated_at: str
