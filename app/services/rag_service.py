from app.core.config import settings
from app.services.vector_store import query_collecion
from app.services.retriever import retrieve
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings


PROMPT = ChatPromptTemplate.from_template("""
Jesteś precyzyjnym asystentem akademickim, który pomaga w analizie dokumentów prawnych i administracyjnych.
Na podstawie poniższych fragmentów z Biuletynu Informacji Publicznej Uniwersytetu Przyrodniczego we Wrocławiu (BIP UPWr), odpowiedz na pytanie użytkownika.

Zawsze opieraj swoją odpowiedź TYLKO i WYŁĄCZNIE na dostarczonych dokumentach, a nie na swojej wiedzy ogólnej. 
Jeśli w dokumentach nie ma odpowiedzi na to pytanie, napisz wprost: "Nie znalazłem takich informacji w udostępnionych dokumentach BIP UPWr."

Dokumenty z BIP UPWr:
{context}

Pytanie użytkownika: 
{question}

Udziel pomocnej i precyzyjnej odpowiedzi, powołując się na konkretne dokumenty (np. numery uchwał, zarządzeń, daty), jeśli są widoczne w tekście powyżej.
""")

LLM = ChatGroq(
        model='llama-3.1-8b-instant', 
        api_key=settings.GROQ_API_KEY, 
        temperature=0.1
    )
EMBEDDINGS_MODEL = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

def answer_question(question : str, top_k : int): 
    query_embedding = EMBEDDINGS_MODEL.embed_query(question)
    raw_results = query_collecion(query_embedding, top_k=top_k)
    sources = retrieve(raw_results)
    context_text = "\n\n".join([source.content_preview for source in sources])
    chain = PROMPT | LLM 
    response = chain.invoke({"context" : context_text, "question" : question})
    return {
        "answer":response.content, 
        "sources":sources
    }