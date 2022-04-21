from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router
from core.config import settings
from db.session import engine, Base


app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)

Base.metadata.create_all(bind=engine)
