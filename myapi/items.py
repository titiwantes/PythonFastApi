from pydantic import BaseModel
from fastapi import  HTTPException

class Item(BaseModel):
    id: str
    name: str

class ItemHandler:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def create_item(self, item: Item):
        try:
            newItem = Item(id=item.id, name=item.name)
            self.items.append(newItem)
            return newItem
        except:
            raise HTTPException(status_code=400, detail="Invalid item")

    def delete_item(self, item_id: str):
        item = next((item for item in self.items if item.id == item_id), None)
        if item is None: raise HTTPException(status_code=404, detail="Item not found")
        self.items.remove(item)
        return item
