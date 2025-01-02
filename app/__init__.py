from fastapi import FastAPI

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# 라우터 불러오기
from app.routes import course, recommendation, user, cost

# 라우터 등록
# 각 기능별 API를 FastAPI 앱에 등록합니다.
app.include_router(course.router, prefix="/api/courses", tags=["Courses"])
app.include_router(recommendation.router, prefix="/api/recommendations", tags=["Recommendations"])
app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(cost.router, prefix="/api/costs", tags=["Costs"])