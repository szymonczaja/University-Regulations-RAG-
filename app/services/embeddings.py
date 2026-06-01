from langchain_huggingface import HuggingFaceEmbeddings
from app.core.config import settings

EMBEDDINGS = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

def get_embeddings(chunks : list) -> list[list[float]]:
    vectors = EMBEDDINGS.embed_documents(chunks) 
    return vectors 