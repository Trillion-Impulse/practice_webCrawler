import requests
from bs4 import BeautifulSoup
import time

# 페이지네이션된 목록에 있는 기사의 제목들을 받아오는 함수
def crawl_title(page):
    # 크롤링할 uRL
    url = f"https://finance.naver.com/news/mainnews.naver?&page={page}"

    # 네이버는 User-Agent 없으면 차단 가능성 있음
    headers = {
        "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
    }

    # HTML GET 요청
    r = requests.get(url,headers=headers)

    # 상태 코드 점검
    if r.status_code != 200:
        print("요청 실패", r.status_code)
        return []
    else:
        print(f"{page} 페이지 크롤링 중 ...")
    
    # BeautifulSoup 객체 생성
    Soup = BeautifulSoup(r.text, "html.parser")

    # 기사 추출
    Articles = Soup.find_all("dd", class_="articleSubject")

    Titles = []
    for i in Articles:
        Title = i.get_text(strip=True)
        Titles.append(Title)
    
    return Titles

# 페이지단위 크롤링
TotalTitles = []
for p in range(1,6):
    print(f"▶ {p} 페이지 크롤링 시작!")
    Titles = crawl_title(p)
    TotalTitles.extend(Titles)
    time.sleep(1)
else:
    print("크롤링 완료 / 전체 기사 수:",len(TotalTitles))

# 상위 5개 기사 제목 미리보기
print("상위 5개 기사 제목 미리보기")
for i, a in enumerate(TotalTitles[:5],1):
    print(f"{i}. {a}")