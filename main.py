from fastapi import FastAPI
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from models import User, Role, Gender


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Lucas",
        last_name="Lucas",
        middle_name="",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Alex",
        middle_name="",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
