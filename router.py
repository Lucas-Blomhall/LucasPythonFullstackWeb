from fastapi import APIRouter, Depends, HTTPException, status, FastAPI
from sqlalchemy.orm import Session

from config import SessionLocal
from datamodel import Car, CarUpdateRequest
from schemas import RequestCar, Response
from sqlalchemyfile import CarModel
import crud


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post('/cars', response_model=Car, status_code=status.HTTP_201_CREATED)
async def create_car(request: RequestCar, db: Session = Depends(get_db)):
    new_car = crud.create_car(db, request.parameter)
    return new_car

@router.get('/cars', response_model=List[Car])
async def read_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db)

@router.get('/cars/{car_id}', response_model=Car)
async def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.put('/cars/{car_id}', response_model=Car)
async def update_car(car_id: int, car_update: CarUpdateRequest, db: Session = Depends(get_db)):
    db_car = crud.update_car(db, car_id, car_update)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.delete('/cars/{car_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(car_id: int, db: Session = Depends(get_db)):
    result = crud.delete_car(db, car_id)
    if not result:
        raise HTTPException(status_code=404, detail="Car not found")