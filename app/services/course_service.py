from app.utils.vector_search import find_similar_places

async def generate_course(request):
    """
    사용자 요청에 따라 추천 코스를 생성합니다.
    - request: CourseRequest (사용자가 입력한 요청 정보)
    """
    recommended_places = find_similar_places(request)  # VectorDB를 사용한 유사도 검색
    return {"course": recommended_places}