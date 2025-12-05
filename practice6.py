from config import PRACTICE_CONFIGS
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 환경변수 설정
try:
    print("환경변수 설정 시작")
    # config 가져옴
    config = PRACTICE_CONFIGS.get("PRACTICE6")
    if not config:
        raise KeyError("PRACTICE_CONFIGS에 PRACTICE6 없음")
    # url 가져옴
    url = config.get("URL")
    if not url:
        raise KeyError("PRACTICE6에 URL 없음")
except KeyError as e:
    print("환경변수 에러:", e)
    sys.exit(1) # 종료코드 1: 환경변수 에러
else:
    print("환경변수 설정 성공")

# ChromeDriver 설정
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# HTML 요청 / 동적 요소 렌더링 대기
driver = None
try:
    print("HTML 요청 시작")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    driver.get(url)
    # JS 로딩 대기하기 위해 WebDriverWait 객체 생성
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#feedRankingContainer a"))
    )
    html = driver.page_source
except Exception as e:
    print("요청 실패:", e)
    sys.exit(2) # 종료코드 2: 드라이버, 네트워크, 렌더링 에러
else:
    print("HTML 요청 성공")
finally:
    if driver:
        driver.quit()

try:
    print("HTML 파싱 시작")
    # BeautifulSoup 객체로 html 파싱
    soup = BeautifulSoup(html, "html.parser")

    news_selector = soup.select("#feedRankingContainer a")
    news_list = []
    for n in news_selector:
        href = n.get("href")
        title_selector = n.select_one("h3.title")
        if href and title_selector:
            title = t if (t:=title_selector.get_text(strip=True)) else "제목 없음"
            news_list.append({
                "title": title,
                "href": href,
            })
except Exception as e:
    print("파싱 실패:", e)
    sys.exit(3) # 종료코드 3: 파싱 에러
else:
    print("HTML 파싱 성공")

# print(soup.prettify()[:300])
# print(news_list)