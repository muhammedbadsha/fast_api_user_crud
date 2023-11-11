from fastapi import FastAPI
from routers.index import router

app = FastAPI(title="User Crud")

app.include_router(router)
