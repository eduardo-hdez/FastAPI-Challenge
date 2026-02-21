from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import engine, Base
from app.models import item
from app.routes import items

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")