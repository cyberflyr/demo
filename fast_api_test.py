# main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{item_id}")
async def root(item_id: int):
    return {"message": "Hello World", "item_id": item_id}
