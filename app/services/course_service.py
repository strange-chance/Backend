from app.utils.vector_search import find_similar_places
from collections import defaultdict

async def generate_course(request):
    """
    사용자 요청에 따라 추천 코스를 생성하고 비용을 계산합니다.
    - request: CourseRequest (사용자가 입력한 요청 정보)
    """
    # VectorDB에서 유사한 장소 추천 받기
    recommended_places = find_similar_places(request)

    # 총 비용 및 카테고리별 비용 계산
    category_totals = defaultdict(int)
    total_cost = 0

    for place in recommended_places:
        # 각 장소의 비용 합산
        category_totals[place["category"]] += place["cost"]
        total_cost += place["cost"]

    # 카테고리별 상세 정보 생성
    details = [{"category": category, "total": total} for category, total in category_totals.items()]

    # 결과 반환
    return {
        "course": recommended_places,  # 추천된 코스 데이터
        "total_cost": total_cost,      # 총 예상 비용
        "details": details             # 카테고리별 상세 비용
    }