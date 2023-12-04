from sqlalchemy import Column, String, Integer, Enum
from config import Base
from datamodel import Car_Type, Engine_Type


class CarModel(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    car_name = Column(String, index=True)
    price = Column(Integer)
    year = Column(String)
    car_type = Column(Enum(Car_Type))
    engine_type = Column(Enum(Engine_Type))
