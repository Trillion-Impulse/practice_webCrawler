import requests
from bs4 import BeautifulSoup

# 크롤링할 URL 
url = "https://n.news.naver.com/mnews/article/011/0004555589"

# 네이버는 User-Agent 없으면 차단 가능성 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# HTML 요청
r = requests.get(url, headers=headers)

# 정상 응답 확인
if r.status_code == 200:
    html = r.text
else:
    print("요청 실패:",r.status_code)
    exit()

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

# 출력
print("기사 제목:", Title)
print("기사 본문:", Body[:100], "...")