from app.core.config import settings 
from fastapi import FastAPI
from app.api.routes_health import router as health_router

app = FastAPI(title=settings.APP_NAME)
app.include_router(health_router)

