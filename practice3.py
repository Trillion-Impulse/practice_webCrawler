from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=None

try:
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

    # 스크롤을 내려서 새 영상이 등장할 때 까지 기다리는 함수
    def wait_for_new_video(driver, before_count, timeout=10):
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "a#video-title-link")) > before_count
        )

    # 무한 루프 및 과부하 방지
    max_scrolls = 20
    scroll_count = 0

    # 무한 스크롤 - 사실상 유한 스크롤
    while scroll_count < max_scrolls:
        scroll_count += 1

        # 스크롤 전 영상 개수
        before = len(driver.find_elements(By.CSS_SELECTOR, "a#video-title-link"))

        # 맨 아래로 스크롤
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # 새 영상이 로딩될 때까지 대기
        try:
            wait_for_new_video(driver, before, timeout=10)
        except TimeoutException:
            print("스크롤 종료")
            break

    # 영상 제목 수집
    title_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title-link")

    # title 속성이 없는 경우 제외하고 모든 title 속성을 가져옴
    titles = [title.strip() for t in title_elements if (title:=t.get_attribute("title"))]

    # 결과 출력
    print(f"총 {len(titles)}개의 영상 제목 수집완료")
    for i,t in enumerate(titles[:10],start=1):
        print(f"{i}. {t}")
    print("...")
    print("마지막.",titles[-1])

except Exception as e:
    print("크롤링 중 예외 발생:", e)

finally:
    # 브라우저 종료
    driver.quit()