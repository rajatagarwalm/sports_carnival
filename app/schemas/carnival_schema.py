from pydantic import BaseModel
from typing import Optional, List
from app.schemas.game_schema import GameOut

class CarnivalCreate(BaseModel):
    carnival_id: str
    name: str
    description: Optional[str]

class CarnivalOut(BaseModel):
    carnival_id: str
    name: str
    description: Optional[str]
    created_at: str
    updated_at: str
    games: List[GameOut] = []
    
class CarnivalUpdate(BaseModel):
    new_carnival_id: str
