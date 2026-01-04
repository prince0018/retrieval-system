# for creating the index and listing all the indices available.
from src.es_client import get_es_client

def create_index(index_name: str, body: dict):
    es = get_es_client()

    if es.indices.exists(index=index_name):
        return {
            "status": "exists",
            "index": index_name
        }

    es.indices.create(index=index_name, body=body)

    return {
        "status": "created",
        "index": index_name
    }



def list_indices():
    es = get_es_client()

    indices = es.indices.get_alias(index="*")
    return list(indices.keys())