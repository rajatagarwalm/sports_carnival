from app.repositories import carnival_repository
from app.models.carnival_model import CarnivalModel
from datetime import datetime

def update_carnival_timestamp(carnival_id):
    carnival_data = carnival_repository.get_carnival(carnival_id)
    if carnival_data:
        carnival = CarnivalModel.from_dict(carnival_data)
        carnival.updated_at = datetime.utcnow().isoformat()
        carnival_repository.save_carnival(carnival)
