from fastapi import Depends, HTTPException, status, FastAPI
from sqlalchemy.orm import Session

from config import SessionLocal
from datamodel import Car, CarUpdateRequest
from sqlalchemyfile import CarModel

# Assuming SessionLocal is defined as in previous examples


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_car(db: Session, car: Car):
    db_car = CarModel(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def get_cars(db: Session):
    return db.query(CarModel).all()


def get_car(db: Session, car_id: int):
    return db.query(CarModel).filter(CarModel.id == car_id).first()


def update_car(db: Session, car_id: int, car_update: CarUpdateRequest):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if db_car:
        update_data = car_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_car, key, value)
        db.commit()
        db.refresh(db_car)
    return db_car


def delete_car(db: Session, car_id: int):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
        return True
    return False


@app.post("/api/v1/cars", response_model=Car, status_code=status.HTTP_201_CREATED)
async def create_car(car: Car, db: Session = Depends(get_db)):
    new_car = CarModel(**car.dict())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


@app.get("/api/v1/cars", response_model=List[Car])
async def read_cars(db: Session = Depends(get_db)):
    return db.query(CarModel).all()


@app.get("/api/v1/cars/{car_id}", response_model=Car)
async def read_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.put("/api/v1/cars/{car_id}", response_model=Car)
async def update_car(car_id: int, car_update: CarUpdateRequest, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    for var, value in vars(car_update).items():
        setattr(car, var, value) if value else None
    db.commit()
    db.refresh(car)
    return car


@app.delete("/api/v1/cars/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(car)
    db.commit()
    return {"detail": "Car deleted"}


# Gammal kod från youtube
# from sqlalchemy.orm import Session
# from datamodel import Car
# from schemas import CarSchema

# def get_car(db:Session, skip:int=0, limit:int=100):
#     return db.query(Car).offset(skip).limit(limit).all()

# def get_car_by_id(db:Session, skip_id: int):
#     return db.query(Car).filter(Car.id == car_id).first()

# def create_car
