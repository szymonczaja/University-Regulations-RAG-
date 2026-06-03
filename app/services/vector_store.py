import chromadb
from app.core.config import settings
import uuid
from typing import Dict

if not settings.CHROMA_PATH.exists():
    settings.CHROMA_PATH.mkdir(parents=True, exist_ok=True)

client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
collection = client.get_or_create_collection(
name='uni-bip', 
metadata={'hnsw:space': 'cosine'}
)

def add_documents(chunks : list, vectors : list, metadatas : list):
    collection.add(
        ids= [uuid.uuid4().hex for x in chunks],
        embeddings=vectors, 
        documents=chunks,
        metadatas=metadatas)
    
def query_collecion(question_embedding : list, top_k : int) -> Dict[str, list]: 
    results = collection.query(
        query_embeddings=question_embedding, 
        n_results=top_k
    )
    return results
