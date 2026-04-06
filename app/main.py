from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base 
from app.api.routes import user

app = FastAPI()

#Create tables
Base.metadata.create_all(bind=engine)

#Include routes 
app.include_router(user.router)