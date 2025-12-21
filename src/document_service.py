from src.es_client import get_es_client
from src.embedding_utils import get_ada002_embedding


def add_document(
    index_name: str,
    content: str
):
    """
    Generate embedding for content and store it in Elasticsearch
    """

    es = get_es_client()

    # 1. Generate embedding
    embedding = get_ada002_embedding(content)

    # 2. Prepare document
    document = {
        "content": content,
        "embedding": embedding
    }

    # 3. Index into Elasticsearch
    response = es.index(
        index=index_name,
        document=document
    )

    return {
        "status": "success",
        "index": index_name,
        "document_id": response["_id"]
    }