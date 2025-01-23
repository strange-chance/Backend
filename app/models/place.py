from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base
from pydantic import BaseModel

# SQLAlchemy 모델: Place
class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)  # 기본 키
    name = Column(String, index=True)  # 장소 이름
    cost = Column(Float)  # 비용
    category = Column(String)  # 카테고리 (예: 식당, 숙소 등)

# Pydantic 모델: PlaceSchema (API 요청/응답용)
class PlaceSchema(BaseModel):
    name: str  # 장소 이름
    cost: float  # 비용
    category: str  # 카테고리 (예: restaurant, hotel 등)

    class Config:
        orm_mode = True  # SQLAlchemy와 호환되도록 설정