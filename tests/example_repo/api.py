from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Read an item by id.
    Returns JSON with item info.
    """
    return {"item_id": item_id}

@app.post("/items")
def create_item(name: str, price: float):
    """Create an item."""
    return {"name": name, "price": price}
