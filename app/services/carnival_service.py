from app.models.carnival_model import CarnivalModel
from app.repositories import carnival_repository
from app.schemas.carnival_schema import CarnivalCreate, CarnivalOut, CarnivalUpdate
from typing import List
from datetime import datetime

def create_carnival(payload: CarnivalCreate) -> CarnivalOut:
    existing = carnival_repository.get_carnival(payload.carnival_id)
    if existing:
        return None
    carnival = CarnivalModel(
        carnival_id=payload.carnival_id,
        name=payload.name,
        description=payload.description
    )
    carnival_repository.save_carnival(carnival)
    return CarnivalOut(**carnival.to_dict())

def get_carnival(carnival_id: str) -> CarnivalOut:
    data = carnival_repository.get_carnival(carnival_id)
    if not data:
        return None
    carnival_model = CarnivalModel.from_dict(data)
    return CarnivalOut(**carnival_model.to_dict())

def list_carnivals() -> List[CarnivalOut]:
    items = carnival_repository.list_carnivals()
    return [CarnivalOut(**CarnivalModel.from_dict(item).to_dict()) for item in items]

def delete_carnival(carnival_id: str) -> bool:
    existing = carnival_repository.get_carnival(carnival_id)
    if not existing:
        return False
    carnival_repository.delete_carnival(carnival_id)
    return True

def update_carnival(carnival_id: str, payload: CarnivalUpdate) -> CarnivalOut:
    # Load existing carnival
    existing = carnival_repository.get_carnival(carnival_id)
    if not existing:
        return None

    # if the ID is not changing
    if carnival_id == payload.new_carnival_id:
        existing["updated_at"] = datetime.utcnow().isoformat()
        # Save the updated record
        carnival_model = CarnivalModel.from_dict(existing)
        carnival_repository.save_carnival(carnival_model)
        return CarnivalOut(**carnival_model.to_dict())

    # ID is changing — check for conflict
    if carnival_repository.get_carnival(payload.new_carnival_id):
        return None

    # Create new item under new ID
    new_data = existing.copy()
    new_data["carnival_id"] = payload.new_carnival_id
    new_data["updated_at"] = datetime.utcnow().isoformat()

    new_carnival_model = CarnivalModel.from_dict(new_data)
    carnival_repository.save_carnival(new_carnival_model)

    # Delete old item
    carnival_repository.delete_carnival(carnival_id)

    return CarnivalOut(**new_carnival_model.to_dict())

