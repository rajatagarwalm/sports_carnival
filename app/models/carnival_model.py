from datetime import datetime

class CarnivalModel:
    def __init__(self, carnival_id, name, description, created_at=None, updated_at=None):
        self.carnival_id = carnival_id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.updated_at = updated_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "carnival_id": self.carnival_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(item):
        return CarnivalModel(
            carnival_id=item["carnival_id"],
            name=item["name"],
            description=item.get("description"),
            created_at=item.get("created_at"),
            updated_at=item.get("updated_at")
        )
