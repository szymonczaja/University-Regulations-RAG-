from fastapi import APIRouter
from app.schemas.ingest import IngestResponse
from app.services.chunking import chunk_text
from app.services.document_loader import extract_text_from_pdf
from app.services.embeddings import get_embeddings
from app.services.vector_store import add_documents
from app.utils.metadata import create_metadata_dict
from app.core.config import BASE_DIR

router = APIRouter() 
DATA_RAW_PATH = BASE_DIR / 'data' / 'raw'

@router.post("/ingest")
def ingest_docs() -> list[IngestResponse]: 
    responses = []
    for file in DATA_RAW_PATH.iterdir(): 
        text = extract_text_from_pdf(file_path=file)
        chunks = chunk_text(document=text) 
        metadatas = []
        for chunk in chunks:
            metadata=create_metadata_dict(file_name=file.name, page_number=0)
            metadatas.append(metadata)
        embeddings = get_embeddings(chunks=chunks)
        add_documents(chunks=chunks, vectors=embeddings, metadatas=metadatas)
        response = IngestResponse(file_name=file.name, chunks_num=len(chunks))
        responses.append(response)
    return responses
