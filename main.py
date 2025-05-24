from fastapi import FastAPI
from routes import item_routes

app = FastAPI()
app.include_router(item_routes.router)
