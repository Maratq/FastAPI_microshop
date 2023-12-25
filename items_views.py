from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/latest/")
def get_latest_item():
    return {
        "item": {"id": 0, "name": "latest"},
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, le=1_000_000)]):
    return {
        "item": {"id": item_id},
    }


@router.get("/")
def list_items():
    return [
        "item1",
        "item2",
        "item2",
    ]
