from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from datamodel import Car, Engine_Type, Car_Type, CarUpdateRequest
from sqlalchemy.orm import Session
import datamodel
from database import SessionLocal, engine, get_db
from sqlalchemyfile import CarModel
from router import router as car_router
from schemas import CreateCarRequest


# Create the database tables
datamodel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.include_router(car_router)

# new code we start with


@app.post("/")
def create(details: CreateCarRequest, db: Session = Depends(get_db)):
    to_create = Car(
        car_name=details.car_name,
        price=details.price,
        year=details.year,
        car_type=details.car_type,
        engine_type=details.engine_type,
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id,
    }
