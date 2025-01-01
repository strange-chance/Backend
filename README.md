# Backend 

### Directory
```
backend/
├── app/
│   ├── __init__.py          # 앱 초기화
│   ├── main.py              # FastAPI 엔트리포인트
│   ├── routes/              # 라우터 디렉토리
│   │   ├── __init__.py
│   │   ├── course.py        # 여행 코스 관련 API
│   │   ├── recommendation.py # 추천 시스템 관련 API
│   │   ├── user.py          # 사용자 관리 API
│   │   └── cost.py          # 경비 계산 API
│   ├── services/            # 비즈니스 로직 처리
│   │   ├── __init__.py
│   │   ├── course_service.py # 코스 생성 로직
│   │   ├── recommendation_service.py # 추천 로직
│   │   ├── user_service.py  # 사용자 관리 로직
│   │   └── cost_service.py  # 경비 계산 로직
│   ├── models/              # 데이터베이스 모델
│   │   ├── __init__.py
│   │   ├── user.py          # 사용자 모델
│   │   ├── course.py        # 코스 모델
│   │   └── place.py         # 장소 모델 (식당, 숙소 등)
│   ├── db/                  # 데이터베이스 초기화 및 관리
│   │   ├── __init__.py
│   │   ├── session.py       # 데이터베이스 세션
│   │   └── models.py        # 모든 모델 import
│   ├── utils/               # 공통 유틸리티
│   │   ├── __init__.py
│   │   ├── vector_search.py # VectorDB 연동 로직
│   │   ├── response.py      # API 응답 포맷
│   │   └── config.py        # 환경 설정
├── tests/                   # 테스트 코드
│   ├── __init__.py
│   ├── test_course.py       # 코스 생성 API 테스트
│   ├── test_recommendation.py # 추천 API 테스트
│   └── test_user.py         # 사용자 관리 테스트
├── requirements.txt         # Python 패키지 의존성
├── .env                     # 환경 변수 파일
└── README.md                # 프로젝트 설명

```