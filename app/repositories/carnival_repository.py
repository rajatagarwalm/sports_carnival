from app.db.dynamodb import get_dynamodb_client
from app.core.tables import DynamoTables

TABLE_NAME = DynamoTables.CARNIVALS

def save_carnival(carnival_model):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    table.put_item(Item=carnival_model.to_dict())

def get_carnival(carnival_id):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    response = table.get_item(Key={"carnival_id": carnival_id})
    return response.get("Item")

def list_carnivals():
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    scan = table.scan()
    return scan.get("Items", [])

def delete_carnival(carnival_id):
    client = get_dynamodb_client()
    table = client.Table(TABLE_NAME)
    table.delete_item(Key={"carnival_id": carnival_id})
