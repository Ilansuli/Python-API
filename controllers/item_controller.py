from core.database import db
from models.item_model import ItemModel
from bson import ObjectId

collection = db["test"]

async def get_all_items():
    items = await collection.find().to_list(100)
    return items

async def create_item(item: dict):
    result = await collection.insert_one(item)
    item["_id"] = result.inserted_id
    return item

async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    return item

async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count
