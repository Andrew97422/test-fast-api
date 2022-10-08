from fastapi import FastAPI
from routers.user_router import user_router

app = FastAPI(
    title='Тестовое приложение',
    version='0.0.1a'
)

app.include_router(user_router)