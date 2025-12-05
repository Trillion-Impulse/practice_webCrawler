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

PRACTICE_CONFIGS={
    "PRACTICE1" : {
        "URL": os.getenv("PRACTICE1_URL")
    },
    "PRACTICE2" : {
        "URL_BASE": os.getenv("PRACTICE2_URL_BASE")
    },
    "PRACTICE3" : {
        "URL": os.getenv("PRACTICE3_URL")
    },
    "PRACTICE4" : {
        "URL": os.getenv("PRACTICE4_URL"),
        "QUERY": os.getenv("PRACTICE4_QUERY"),
        "REFERER_BASE": os.getenv("PRACTICE4_REFERER_BASE")
    },
    "PRACTICE5" : {
        "URL_BASE": os.getenv("PRACTICE5_URL_BASE")
    },
    "PRACTICE6" : {
        "URL": os.getenv("PRACTICE6_URL")
    },
}