from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.services.rag_service import answer_question

router = APIRouter()

@router.post("/ask")
def ask_question(data : QueryRequest) -> QueryResponse:
    answer = answer_question(data.question, data.top_k)
    query_response = QueryResponse(answer=answer['answer'], sources=answer['sources'])
    return query_response