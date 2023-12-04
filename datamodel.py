from typing import Optional, List
# from uuid import UUID, uuid4
# id = Column(UUID, primary_key=True, index=True, default=uuid4)
# id: Optional[UUID] = uuid4

from pydantic import BaseModel
from enum import Enum
from config import Base


class Engine_Type(str, Enum):
    fuel = "fuel"
    electric = "electric"


class Car_Type(str, Enum):
    sedan = "sedan"
    suv = "suv"
    sport = "sport"


class Car(BaseModel):
    id: Optional[int]
    car_name: str
    price: int
    year: str
    car_type: Car_Type
    engine_type: Engine_Type


class CarUpdateRequest(BaseModel):
    car_name: Optional[str]
    price: Optional[int]
    year: Optional[str]
    car_type: Optional[Car_Type]
    engine_type: Optional[Engine_Type]