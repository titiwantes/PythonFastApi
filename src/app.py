from fastapi import FastAPI, HTTPException
from typing import List
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import CustomMiddleware
from items import ItemHandler, Item

item_handler = ItemHandler()

app = FastAPI()
middleware = CustomMiddleware()
app.add_middleware(BaseHTTPMiddleware, dispatch=middleware)


@app.get("/items/", response_model=List[Item])
async def get_items():
    return item_handler.get_items()

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
   return item_handler.create_item(item)

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: str):
    return item_handler.delete_item(item_id)