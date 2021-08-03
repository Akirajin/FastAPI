from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_user(users_id: int):
    return {"item_id": item_id}
