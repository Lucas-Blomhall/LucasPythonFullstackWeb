from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from models import Car, Engine_Type, Car_Type, CarUpdateRequest
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# id: Optional[UUID] = uuid4
#     car_name: str
#     price: int
#     year: str
#     car_type: Car_Type
#     engine_type: List[Engine_Type]

db: List[Car] = [
    Car(
        id=uuid4(),
        car_name="Audi",
        price=100000,
        year="2002",
        car_type=Car_Type.sedan,
        engine_type=Engine_Type.fuel
    ),
    Car(
        id=uuid4(),
        car_name="Tesla",
        price=100000,
        year="2018",
        car_type=Car_Type.sedan,
        engine_type=Engine_Type.electric
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/v1/cars")
async def fetch_cars(db: Session = Depends(get_db)):
    return db.query(CarModel)


@app.post("/api/v1/cars", status_code=201)
async def register_cars(car: Car):
    db.append(car)


@app.delete("/api/v1/cars/{car_id}", status_code=204)
async def delete_car(car_id: UUID):
    for car in db:
        if car.id == car_id:
            db.remove(car)
            return
        raise HTTPException(
            status_code=404,
            detail=f"car with id {car_id} does not exist"
        )


@app.put("/api/v1/cars/{car_id}")
async def update_car(car_update: CarUpdateRequest, car_id: UUID):
    for car in db:
        if car.id == car_id:
            if car_update.car_name is not None:
                car.car_name = car_update.car_name
            if car_update.price is not None:
                car.price = car_update.price
            if car_update.year is not None:
                car.year = car_update.year
            if car_update.car_type is not None:
                car.car_type = car_update.car_type
            if car_update.engine_type is not None:
                car.engine_type = car_update.engine_type
            return
    raise HTTPException(
        status_code=404,
        detail=f"car with id: {car_id} does not exists"
    )
