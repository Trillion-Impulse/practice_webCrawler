import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
from config import PRACTICE_CONFIGS

url_base = PRACTICE_CONFIGS.get("PRACTICE5").get("URL_BASE")

# 동기
# 페이지네이션된 목록에 있는 기사의 제목들을 받아오는 함수
def crawl_title_sync(page, max_retries=3, delay=2):
    # 크롤링할 URL
    url = f"{url_base}?&page={page}"

    # 네이버는 User-Agent 없으면 차단 가능성 있음
    headers = {
        "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"{page} 페이지 크롤링 중 ...")

    attempt = 0
    while attempt < max_retries:
        attempt+=1
        try:
            # HTML GET 요청
            r = requests.get(url,headers=headers, timeout=5)
            # 상태 코드 점검
            if r.status_code == 200:
                html = r.text
                break # 요청 성공 시 반복 종료
            else:
                print(f"요청 실패 (상태 코드: {r.status_code}) - {attempt}/{max_retries} 재시도")
        except requests.exceptions.RequestException as e:
            print(f"예외 발생: {e} - {attempt}/{max_retries} 재시도")
        time.sleep(delay)
    else:
        print(f"크롤링 실패: {url}")
        return []
    
    # BeautifulSoup 객체 생성
    Soup = BeautifulSoup(html, "html.parser")

    # 기사 추출
    Articles = Soup.find_all("dd", class_="articleSubject")

    # 기사 제목 추출
    Titles_sync = [t.get_text(strip=True)for t in Articles]
    
    return Titles_sync

# 실행 및 시간 측정
sync_start_time = time.time()
TotalTitles_sync = []
for p in range(1,6):
    print(f"▶ {p} 페이지 크롤링 시작!")
    Titles_sync = crawl_title_sync(p)
    TotalTitles_sync.extend(Titles_sync)
else:
    print("동기 크롤링 완료 / 전체 기사 수:",len(TotalTitles_sync))
sync_end_time = time.time()



# 비동기
# 페이지네이션된 목록에 있는 기사들의 제목을 받아오는 비동기 함수
async def crawl_title_async(session, page, max_retries=3, delay=2):
    # 크롤링할 URL
    url = f"{url_base}?&page={page}"

    # 네이버는 User-Agent 없으면 차단 가능성 있음
    headers = {
        "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"{page} 페이지 크롤링 중 ...")

    attempt = 0
    while attempt < max_retries:
        attempt+=1
        try:
            # 비동기 GET 요청
            async with session.get(url,headers=headers, timeout=5) as r:
                # 상태 코드 점검
                if r.status == 200:
                    html = await r.text()
                    # BeautifulSoup 객체 생성
                    Soup = BeautifulSoup(html, "html.parser")

                    # 기사 추출
                    Articles = Soup.find_all("dd", class_="articleSubject")

                    # 기사 제목 추출
                    Titles_async = [t.get_text(strip=True)for t in Articles]
    
                    return Titles_async
                else:
                    print(f"요청 실패 (상태 코드: {r.status}) - {attempt}/{max_retries} 재시도")
        except aiohttp.ClientError as e:
            print(f"{page} 페이지 예외 발생: {e} - {attempt}/{max_retries} 재시도")
        await asyncio.sleep(delay)
    else:
        print(f"크롤링 실패: {url}")
        return []

# 메인 비동기 함수
async def main():
    pages_to_crawl = 5
    TotalTitles_async = []

    async with aiohttp.ClientSession() as session:
        tasks = [crawl_title_async(session, page) for page in range(1, pages_to_crawl+1)]
        results = await asyncio.gather(*tasks)

    for Titles in results:
        TotalTitles_async.extend(Titles)
    else:
        print("비동기 크롤링 완료 / 전체 기사 수:",len(TotalTitles_async))
    
    return TotalTitles_async

# 실행 및 시간 측정
async_start_time = time.time()
TotalTitles_async = asyncio.run(main())
async_end_time = time.time()



# 크롤링 시간 출력
print(f"동기 크롤링 소요 시간: {sync_end_time - sync_start_time:.3f}초")
print(f"비동기 크롤링 소요 시간: {async_end_time - async_start_time:.3f}초")