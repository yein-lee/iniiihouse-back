from fastapi import APIRouter

from .routes import login, register, party

api_router: APIRouter = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(register.router, tags=["register"])
api_router.include_router(party.router, prefix="/party", tags=["party"])
