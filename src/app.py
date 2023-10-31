from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import datetime
from middleware import Middleware

app = FastAPI()
app.add_middleware(Middleware)


class Item(BaseModel):
    id: str
    name: str

items = []

@app.get("/items/", response_model=List[dict])
async def get_items():
    return items

@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    try:
        newItem = Item(id=item.id, name=item.name)
        items.append(newItem.model_dump())
        return newItem.model_dump()
    except:
        raise HTTPException(status_code=400, detail="Invalid item")

@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: str):
    print (items, item_id)
    item = next((item for item in items if item["id"] == item_id), None)
    print(item)
    if item is None: raise HTTPException(status_code=404, detail="Item not found")
    items.remove(item)
    return item

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = datetime.datetime.utcnow()
    response = await call_next(request)
    end_time = datetime.datetime.utcnow()
    print(f"method:{request.method} url:{request.url} status_code:{response.status_code} start:{start_time} end:{end_time} ")
    return response