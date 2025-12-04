import requests
from bs4 import BeautifulSoup
import sys
import logging
from config import PRACTICE_CONFIGS

logging.basicConfig(
    filename="crawler.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

# 크롤링할 URL을 config에서 가져옴
url = PRACTICE_CONFIGS.get("PRACTICE1").get("URL")

# User-Agent 없으면 차단 가능성 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    logging.info(f"크롤링 시작: {url}")
    # HTML 요청
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    html = r.text
except requests.exceptions.RequestException as e:
    logging.error(f"HTTP 요청 실패: {e}")
    print("요청 실패:",e)
    sys.exit(1) # 종료 코드 1: 네트워크/HTTP 오류

try:
    # beautifulsoup 객체 생성
    soup = BeautifulSoup(html, "html.parser")

    # 기사 제목 추출 (class 기반)
    TitleTag = soup.find("h2", class_="media_end_head_headline")
    Title = TitleTag.get_text(strip=True) if TitleTag else "제목 없음"

    # 기사 본문 추출 (id 기반)
    ArticleTag = soup.find("article", id="dic_area")
    if ArticleTag:
        for br in ArticleTag.find_all("br"):
            br.replace_with("\n")
        Body = ArticleTag.get_text(strip=True)
    else:
        Body = "본문 없음"
    
    logging.info("HTML 파싱 완료")
except Exception as e:
    logging.error(f"HTML 파싱 실패: {e}")
    sys.exit(2) # 종료 코드 2: 파싱 오류

# 출력
print("기사 제목:", Title)
print("기사 본문:", Body[:100], "...")
logging.info("크롤링 완료")

# BeautifulSoup이 실제로 HTMl을 어떻게 구조화했는지, soup 객체 살펴보기
print(soup.prettify()[:500])

# BeautifulSoup이 제공하는 단축속성 중 title
print(soup.title)

# title 태그 안의 순수 텍스트만 추출
print(soup.title.get_text())

# 위에 기사 본문에서 특정 태그 추출
print(ArticleTag)

# 태그의 이름
print(ArticleTag.name)

# 태그의 속성 딕셔너리
print(ArticleTag.attrs)

# 태그의 속성 직접 접근, 딕셔너리 형태이므로 ['키']의 형태
print(ArticleTag['id'])

# 추출한 태그 내부 하위 태그 탐색
print(ArticleTag.find_all("img"))

# 찾은 하위 태그 속성 dict의 key로 직접 접근
for img in ArticleTag.find_all("img"):
    print(img['data-src'])

# CSS selector 기반 데이터 추출 및 get을 통한 안전한 접근
ArticleTag_select = soup.select("article#dic_area img")
for img in ArticleTag_select:
    print(img.get("data-src"))