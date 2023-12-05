from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from sqlalchemy import Integer, String
from sqlalchemy.schema import Column
from database import Base
from sqlalchemy.dialects.postgresql import ENUM

from datamodel import Car_Type, Engine_Type


class Car(BaseModel):
    id: int
    car_name: str
    price: int
    year: str
    car_type: Car_Type
    engine_type: Engine_Type

    class Config:
        orm_mode = True

# older code


class CarSchemaNew(Base):
    __tablename__ = "cars"
    id: Column(Integer, primary_key=True)
    car_name: Column(String, nullable=False)
    price: Column(Integer, nullable=False)
    year: Column(String, nullable=False)
    car_type: Column(Car_Type, nullable=False)
    engine_type: Column(Engine_Type, nullable=False)


T = TypeVar('T')


class CarSchema(BaseModel):
    __tablename__ = "cars"

    id: Column(Integer)
    car_name: Optional[str] = None
    price: Optional[int] = None
    year: Optional[str] = None
    car_type: Optional[Car_Type] = None
    engine_type: Optional[Engine_Type] = None

    class Config:
        orm_mode = True


class RequestCar(BaseModel):
    parameter: CarSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


# SQLalchemy model that defines database schema SQLalchemy = schemas.
class CarSchema(Base):
    __tablename__ = "cars"
    id: Column(Integer, primary_key=True, index=True, autoincrement=True)
    car_name: Column(String, nullable=False)
    price: Column(Integer, nullable=False)
    year: Column(String, nullable=False)
    car_type = Column(ENUM('sedan', 'suv', 'sport',
                      name='car_types'), nullable=False)
    engine_type = Column(
        ENUM('fuel', 'electric', name='engine_types'), nullable=False)


Base.metadata.create_all(bind=engine)
