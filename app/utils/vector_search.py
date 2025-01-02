def query_vector_db(category, preferences):
    """
    VectorDB에서 유사한 장소를 검색합니다.
    - category: 장소 카테고리 (식당, 숙소 등)
    - preferences: 사용자 선호 옵션
    """
    # 예제 데이터 반환 (실제 VectorDB 연동 필요)
    return [
        {"name": "Example Place 1", "category": category, "preferences": preferences},
        {"name": "Example Place 2", "category": category, "preferences": preferences},
    ]
    
def find_similar_places(request):
    """
    사용자 요청에 기반하여 유사한 장소를 반환하는 함수 (예제 데이터 사용).
    - request: 사용자 입력 데이터
    """
    # Mock 데이터 반환 (VectorDB 연동 전 기본 값)
    return [
        {"name": "Example Place 1", "cost": 10000, "category": "restaurant"},
        {"name": "Example Place 2", "cost": 15000, "category": "hotel"}
    ]