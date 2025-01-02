import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # 기본 SQLite 설정
VECTOR_DB_URL = os.getenv("VECTOR_DB_URL", "http://localhost:8000")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret_key")
PASSWORD_SALT = os.getenv("PASSWORD_SALT", "default_salt")