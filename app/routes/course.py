from fastapi import APIRouter
from app.services.course_service import generate_course
from app.models.course import CourseRequest

# 코스 생성 라우터
router = APIRouter()

@router.post("/")
async def create_course(request: CourseRequest):
    """
    사용자 요청에 따라 여행 코스를 생성합니다.
    - request: CourseRequest (사용자가 입력한 여행 정보)
    """
    return await generate_course(request)