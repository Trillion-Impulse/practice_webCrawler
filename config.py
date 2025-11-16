import os
from dotenv import load_dotenv

# .env 파일 읽기
load_dotenv()

# DB 설정을 딕셔너리로 정리
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "charset": os.getenv("DB_CHARSET", "utf8mb4")
}