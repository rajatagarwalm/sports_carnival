from app.db.dynamodb import get_dynamodb_client
from app.core.tables import DynamoTables

TABLE_NAME = DynamoTables.GAMES

def save_game(game_model):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    table.put_item(Item=game_model.to_dict())

def get_game(carnival_id, game_id):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    response = table.get_item(Key={"carnival_id": carnival_id, "game_id": game_id})
    return response.get("Item")

def list_games(carnival_id):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    response = table.query(
        KeyConditionExpression="carnival_id = :cid",
        ExpressionAttributeValues={":cid": carnival_id}
    )
    return response.get("Items", [])

def delete_game(carnival_id, game_id):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    table.delete_item(Key={"carnival_id": carnival_id, "game_id": game_id})
