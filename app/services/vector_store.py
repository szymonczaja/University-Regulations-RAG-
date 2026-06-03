import chromadb
from app.core.config import settings

client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
collection = client.get_or_create_collection(
    name='uni-bip', 
    metadata={'hnsw:space': 'cosine'}
)