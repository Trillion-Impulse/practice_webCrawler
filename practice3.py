from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 유튜브 메인 페이지 접속
driver.get("https://www.youtube.com/")
wait = WebDriverWait(driver, 10) # 최대 10초 기다림

# 왼쪽 네비게이션에서 "스포츠" 클릭
sport_tab = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), '스포츠') or contains(text(), 'Sports')]"))
)
sport_tab.click()

# 스포츠 탭 클릭 후 로딩 대기
time.sleep(2)

# 스크롤 끝까지 내리기
prev_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # 스크롤 맨 아래로 이동
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2) # 로딩 대기

    # 현재 높이
    curr_height = driver.execute_script("return document.documentElement.scrollHeight")

    # 더 이상 증가 없다면 스크롤 종료
    if curr_height == prev_height:
        print("모든 영상 로딩 완료")
        print("스크롤 종료")
        break

    prev_height = curr_height

# 영상 제목 크롤링
title_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title-link")

# title 속성이 없는 경우 제외하고 모든 title 속성을 가져옴
titles = [title.strip() for t in title_elements if (title:=t.get_attribute("title"))]

# 결과 출력
print(f"총 {len(titles)}개의 영상 제목 수집완료")
for i,t in enumerate(titles[:10],start=1):
    print(f"{i}. {t}")
print("...")
print("마지막.",titles[-1])

# 브라우저 종료
driver.quit()