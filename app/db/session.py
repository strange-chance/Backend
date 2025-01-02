from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.config import DATABASE_URL  # 환경 변수에서 데이터베이스 URL 가져오기

# 데이터베이스 엔진 생성
# DATABASE_URL은 .env 파일에서 설정한 값입니다.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # 모든 ORM 모델의 베이스 클래스

def db_session():
    """데이터베이스 세션 생성 및 관리"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def init_db():
    """데이터베이스 초기화"""
    # 데이터베이스 테이블 생성
    # 모든 모델을 import하여 테이블 생성
    from app.models import user, course
    Base.metadata.create_all(bind=engine)