# we will going to create a rag system with overall software cycle

# payload
# for creating the index
{
  "index_name": "rag",
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text"
      },
      "embedding": {
        "type": "dense_vector",
        "dims": 1536,
        "index": true,
        "similarity": "cosine"
      }
    }
  }
}


1. Install the requirements.txt
2. Install the docker
3. Create the docker-compose.yml file
4. docker compose up -d
