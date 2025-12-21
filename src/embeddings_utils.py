from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_EMBEDDINGS"]
)

def get_ada002_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding