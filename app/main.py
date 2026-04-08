from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base 
from app.api.routes import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#Create tables
Base.metadata.create_all(bind=engine)

#Include routes 
app.include_router(user.router)