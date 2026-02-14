from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")