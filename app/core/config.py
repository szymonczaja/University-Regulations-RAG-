from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    APP_NAME : str = 'UNI RAG'
    GROQ_API_KEY : str
    CHROMA_PATH : Path = BASE_DIR / 'data' / 'chroma'
    EMBEDDING_MODEL : str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()
