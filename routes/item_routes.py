from fastapi import APIRouter, HTTPException
from controllers import item_controller
from models.item_model import ItemModel

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=list[ItemModel])
async def get_items():
    return await item_controller.get_all_items()

@router.post("/", response_model=ItemModel)
async def add_item(item: ItemModel):
    return await item_controller.create_item(item.dict())

@router.get("/{item_id}", response_model=ItemModel)
async def get_item(item_id: str):
    item = await item_controller.get_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    deleted = await item_controller.delete_item(item_id)
    if deleted:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
