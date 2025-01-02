import sys
import uvicorn
from app import app  # FastAPI 앱 인스턴스 불러오기
from app.db.session import init_db  # 데이터베이스 초기화 함수 불러오기

# PYTHONPATH에 현재 경로 추가
# Python 모듈 경로 문제를 해결하기 위해 sys.path에 현재 디렉토리를 추가
sys.path.append(".")

# 데이터베이스 초기화
# 앱 실행 전에 데이터베이스 스키마를 생성합니다.
init_db()

if __name__ == "__main__":
    # FastAPI 서버 실행
    # Uvicorn을 사용해 FastAPI 애플리케이션을 실행합니다.
    uvicorn.run(app, host="0.0.0.0", port=8000)