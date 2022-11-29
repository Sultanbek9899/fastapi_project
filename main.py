from fastapi import FastAPI
from api import service_router
app = FastAPI()


app.router(service_router)