from fastapi import APIRouter, HTTPException, status
from app.controllers import item_controller
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item_data: ItemCreate):
    """Create a new item"""
    item = await item_controller.create_item(item_data)
    return item

@router.get("/", response_model=list[ItemResponse])
async def get_items():
    """Get all items"""
    items = await item_controller.get_all_items()
    return items
    
@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    "Get a single item by ID"
    item = await item_controller.get_item_by_id(item_id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found"
        )

    return item
    
@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item_data: ItemUpdate):
    """Update an existing item by ID"""
    item = await item_controller.update_item(item_id, item_data)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found"
        )
    
    return item

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    """Delete an item by ID"""
    item = await item_controller.delete_item(item_id)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found"
        )
    
    return {"message": "Item deleted successfully",
            "deleted_item": item
    }