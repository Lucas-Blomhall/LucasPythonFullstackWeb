from sqlalchemy import create_engine, Column, String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datamodel import Car_Type, Engine_Type

DATABASE_URL = "postgresql://postgres:Vanligt123!@localhost/carappdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# class CarModel(Base):
#     __tablename__ = "cars"

#     id = Column(UUID, primary_key=True, index=True, default=uuid4)
#     car_name = Column(String, index=True)
#     price = Column(Integer)
#     year = Column(String)
#     car_type = Column(Enum(Car_Type))
#     engine_type = Column(Enum(Engine_Type))


# # Create the database tables
# Base.metadata.create_all(bind=engine)
