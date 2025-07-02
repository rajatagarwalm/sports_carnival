from fastapi import APIRouter, HTTPException
from app.services import carnival_service
from typing import List
from app.schemas.carnival_schema import CarnivalCreate, CarnivalOut, CarnivalUpdate

router = APIRouter()

@router.post("/carnivals", response_model=CarnivalOut)
def create_carnival(payload: CarnivalCreate):
    result = carnival_service.create_carnival(payload)
    if not result:
        raise HTTPException(status_code=400, detail="Carnival already exists")
    return result

@router.get("/carnivals/{carnival_id}", response_model=CarnivalOut)
def get_carnival(carnival_id: str):
    carnival = carnival_service.get_carnival(carnival_id)
    if not carnival:
        raise HTTPException(status_code=404, detail="Carnival not found")
    return carnival

@router.get("/carnivals", response_model=List[CarnivalOut])
def list_carnivals():
    return carnival_service.list_carnivals()

@router.delete("/carnivals/{carnival_id}", response_model=dict)
def delete_carnival(carnival_id: str):
    success = carnival_service.delete_carnival(carnival_id)
    if not success:
        raise HTTPException(status_code=404, detail="Carnival not found")
    return {"message": "Carnival deleted successfully"}

@router.put("/carnivals/{carnival_id}", response_model=CarnivalOut)
def update_carnival(carnival_id: str, payload: CarnivalUpdate):
    result = carnival_service.update_carnival(carnival_id, payload)
    if not result:
        raise HTTPException(status_code=404, detail="Carnival not found or new ID already exists")
    return result