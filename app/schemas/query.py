from pydantic import BaseModel, ConfigDict
from typing import List

class QueryRequest(BaseModel):
    question : str 
    top_k : int = 5
    model_config = ConfigDict(extra='ignore')

class Source(BaseModel):
    document : str 
    page : int 
    section : str 
    content_preview : str 

class QueryResponse(BaseModel):
    answer : str 
    sources : List[Source]
    model_config = ConfigDict(extra='ignore')