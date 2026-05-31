from pydantic import BaseModel, ConfigDict

class IngestResponse(BaseModel):
    file_name : str 
    chunks_num : int
    model_config = ConfigDict(extra='ignore')