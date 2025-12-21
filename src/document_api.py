from fastapi import APIRouter, HTTPException
from src.document_service import add_document

router = APIRouter()


@router.post("/documents/add")
def add_document_api(payload: dict):
    """
    Payload:
    {
      "index_name": "rag_ada002_v1",
      "content": "Text to embed and store"
    }
    """

    index_name = payload.get("index_name")
    content = payload.get("content")

    if not index_name or not content:
        raise HTTPException(
            status_code=400,
            detail="index_name and content are required"
        )

    return add_document(index_name=index_name, content=content)