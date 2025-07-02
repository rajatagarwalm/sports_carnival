from fastapi import FastAPI
from app.api.v1 import carnival_controller, game_controller

app = FastAPI()

app.include_router(carnival_controller.router, prefix="/api/v1")
app.include_router(game_controller.router, prefix="/api/v1")