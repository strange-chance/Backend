from pydantic import BaseModel
from typing import List
from app.models.place import PlaceSchema 
from app.db.session import Base

# 코스 요청 모델
class CourseRequest(BaseModel):
    start_location: str  # 시작 위치
    end_location: str  # 종료 위치
    participants: int  # 참여 인원
    days: int  # 여행 기간
    preferences: dict  # 사용자 선호 옵션
    stops: List[PlaceSchema]  # 경유지 목록