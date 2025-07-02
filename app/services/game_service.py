from app.models.game_model import GameModel
from app.repositories import game_repository
from app.schemas.game_schema import GameCreate, GameOut, GameUpdate
from app.utils.game_utils import update_carnival_timestamp
from datetime import datetime

def create_game(carnival_id, payload: GameCreate) -> GameOut:
    existing = game_repository.get_game(carnival_id, payload.game_id)
    if existing:
        return None

    game = GameModel(
        carnival_id=carnival_id,
        game_id=payload.game_id,
        name=payload.name,
        categories=payload.categories
    )
    game_repository.save_game(game)
    
    update_carnival_timestamp(carnival_id)
    
    return GameOut(**game.to_dict())

def get_game(carnival_id, game_id) -> GameOut:
    data = game_repository.get_game(carnival_id, game_id)
    if not data:
        return None
    model = GameModel.from_dict(data)
    return GameOut(**model.to_dict())

def list_games(carnival_id):
    items = game_repository.list_games(carnival_id)
    return [GameOut(**GameModel.from_dict(item).to_dict()) for item in items]

def delete_game(carnival_id, game_id):
    existing = game_repository.get_game(carnival_id, game_id)
    if not existing:
        return False
    game_repository.delete_game(carnival_id, game_id)
    
    update_carnival_timestamp(carnival_id)

    return True

def update_game(carnival_id, game_id, payload: GameUpdate):
    existing = game_repository.get_game(carnival_id, game_id)
    if not existing:
        return None

    model = GameModel.from_dict(existing)

    new_game_id = payload.new_game_id or game_id

    # if game_id is changing
    if new_game_id != game_id:
        # check for conflict
        if game_repository.get_game(carnival_id, new_game_id):
            return None

        # create new item with new_game_id
        new_model = GameModel(
            carnival_id=carnival_id,
            game_id=new_game_id,
            name=payload.name or model.name,
            categories=payload.categories or model.categories,
            created_at=model.created_at,
            updated_at=datetime.utcnow().isoformat(),
        )
        game_repository.save_game(new_model)

        # delete old game
        game_repository.delete_game(carnival_id, game_id)
        
        update_carnival_timestamp(carnival_id)

        return GameOut(**new_model.to_dict())

    # else: same game_id → update in place
    if payload.name:
        model.name = payload.name
    if payload.categories:
        model.categories = payload.categories

    model.updated_at = datetime.utcnow().isoformat()
    game_repository.save_game(model)

    return GameOut(**model.to_dict())

