import sqlalchemy
from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Coordenadas(Base):
    __tablename__ = 'Coordenadas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

    def __repr__(self):
        return f"User(id={self.id}, x={self.x}, y={self.y}, z={self.z})"
