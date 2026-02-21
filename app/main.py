from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import engine, Base
from app.models import item
from app.routes import items

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kalmy Items API",
    description="""
## Items API

REST API for item management. Allows you to **create**, **read**, **update** and **delete** items.

### Features
- Full CRUD operations on items
- Pagination with `skip` and `limit`
- Automatic validation with Pydantic
"""
)

app.include_router(items.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")