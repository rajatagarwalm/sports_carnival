from datetime import datetime

class GameModel:
    def __init__(self, carnival_id, game_id, name, categories, created_at=None, updated_at=None):
        self.carnival_id = carnival_id
        self.game_id = game_id
        self.name = name
        self.categories = categories
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.updated_at = updated_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "carnival_id": self.carnival_id,
            "game_id": self.game_id,
            "name": self.name,
            "categories": self.categories,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(item):
        return GameModel(
            carnival_id=item["carnival_id"],
            game_id=item["game_id"],
            name=item["name"],
            categories=item["categories"],
            created_at=item.get("created_at"),
            updated_at=item.get("updated_at"),
        )
