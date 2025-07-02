from fastapi import APIRouter, HTTPException
from app.services import carnival_service
from typing import List
from app.schemas.carnival_schema import CarnivalCreate, CarnivalOut, CarnivalUpdate

router = APIRouter()

@router.post("/carnivals", response_model=CarnivalOut)
def create_carnival(payload: CarnivalCreate):
    try:
        result = carnival_service.create_carnival(payload)
        if not result:
            raise HTTPException(status_code=400, detail="Carnival already exists")
        return result
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/carnivals/{carnival_id}", response_model=CarnivalOut)
def get_carnival(carnival_id: str):
    try:
        carnival = carnival_service.get_carnival(carnival_id)
        if not carnival:
            raise HTTPException(status_code=404, detail="Carnival not found")
        return carnival
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/carnivals", response_model=List[CarnivalOut])
def list_carnivals():
    try:
        return carnival_service.list_carnivals()
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/carnivals/{carnival_id}", response_model=dict)
def delete_carnival(carnival_id: str):
    try:
        success = carnival_service.delete_carnival(carnival_id)
        if not success:
            raise HTTPException(status_code=404, detail="Carnival not found")
        return {"message": "Carnival deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/carnivals/{carnival_id}", response_model=CarnivalOut)
def update_carnival(carnival_id: str, payload: CarnivalUpdate):
    try:
        result = carnival_service.update_carnival(carnival_id, payload)
        if not result:
            raise HTTPException(status_code=404, detail="Carnival not found or new ID already exists")
        return result
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")