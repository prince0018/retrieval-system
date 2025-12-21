from fastapi import APIRouter, HTTPException
from src.index_service import create_index, list_indices

router = APIRouter()

@router.post("/create")
def create_index_api(payload: dict):
    index_name = payload.get("index_name")
    mappings = payload.get("mappings")
    settings = payload.get("settings", {})

    if not index_name or not mappings:
        raise HTTPException(
            status_code=400,
            detail="index_name and mappings are required"
        )

    body = {"mappings": mappings}
    if settings:
        body["settings"] = settings

    return create_index(index_name=index_name, body=body)


@router.get("")
def list_all_indices():
    """
    List all Elasticsearch indices
    """
    return {
        "indices": list_indices()
    }