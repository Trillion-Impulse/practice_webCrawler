import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

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

# csv 파일로 저장 - pandas 사용
df = pd.DataFrame({"title":TotalTitles})
filename_for_pandas = f"news_titles_pandas_{int(time.time())}.csv"
df.to_csv(filename_for_pandas, index=False, encoding="utf-8-sig") # utf-8로 하면 엑셀에서 한글 깨짐

# csv 파일로 저장 - csv 모듈 사용 - writerow
filename_for_csv_writerow = f"news_titles_csv_writerow_{int(time.time())}.csv"
with open(filename_for_csv_writerow, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["title"])
    for t in TotalTitles:
        writer.writerow([t])

# csv 파일로 저장 - csv 모듈 사용 - writerows
filename_for_csv_writerows = f"news_titles_csv_writerows_{int(time.time())}.csv"
rows = [[t]for t in TotalTitles] # writerows는 리스트의 리스트를 받아야함
with open(filename_for_csv_writerows, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["title"])
    writer.writerows(rows)

# csv 파일로 저장 - csv 모듈 사용 - DictWriter
filename_for_csv_DictWriter = f"news_titles_csv_dictwriter_{int(time.time())}.csv"
dict_rows = [{"title":t}for t in TotalTitles]
with open(filename_for_csv_DictWriter,"w",newline="",encoding="utf-8-sig") as f:
    fieldnames = ["title"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader() # dictwriter 전용 메서드로 fieldnames 리스트에 있는 값을 자동으로 csv 첫 줄로 써줌
    writer.writerows(dict_rows) # writerow도 가능