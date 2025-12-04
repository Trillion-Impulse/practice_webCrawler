import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from config import PRACTICE_CONFIGS


# 검색어
query = PRACTICE_CONFIGS.get("PRACTICE4").get("QUERY")
# 요청 URL
url = PRACTICE_CONFIGS.get("PRACTICE4").get("URL")

# Devtools에서 확인한 Query String Parameters
params = {
    "query": "query",  # 검색어
    "start": 1,          # 시작 뉴스 번호
    "sort": 0,            # 정렬 방식
    "nso": "so:r,p:all,a:all"  # 기간/뉴스 타입 등
}

# Referer에 query를 포함할 경우 반드시 URL 인코딩
referer_base = PRACTICE_CONFIGS.get("PRACTICE4").get("REFERER_BASE")
referer = f"{referer_base}?where=news&query={quote(query)}"

# 브라우저처럼 보이게 User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": referer,
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest"
    }

# 쿠키: 필수 가능성이 높은 것만 사용
cookies = {
    "NNB": "JRCSWKUDHQJGG",
    "page_uid": "jfagrwqo15Vss4l/afsssssssow-138069"
}

# Session 생성 (쿠키 자동 관리)
session = requests.Session()

# GET 요청 보내기
response = session.get(url, params=params, headers=headers, cookies=cookies)

print("상태코드", response.status_code)
print("응답길이:",len(response.text))

try:
    # JSON 데이터로 파싱
    data = response.json()

    # HTML fragment 추출
    html_fragment = data["collection"][0]["html"]

    # BeautifulSoup HTML 파싱 객체 생성
    soup = BeautifulSoup(html_fragment, "html.parser")

    print(soup.prettify()[:1000])
except ValueError:
    print("JSON 파싱 실패, 응답 내용:", response.text[:500])