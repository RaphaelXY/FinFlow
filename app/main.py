from fastapi import FastAPI
from . import models, database
from .routes import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FinFlow - Microserviço Financeiro")
app.include_router(router)