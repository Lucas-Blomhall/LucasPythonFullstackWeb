from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from datamodel import Car_Type, Engine_Type

T = TypeVar('T')


class CarSchema(BaseModel):
    __tablename__ = "cars"

    id: Optional[int] = None
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
