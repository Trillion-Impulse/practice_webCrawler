# practice_webCrawler
***
## with python
1. 주요 도구 및 라이브러리
    1. Requests: HTTP 요청을 보내는 라이브러리로, 페이지 내용을 가져오는 데 사용
    1. BeautifulSoup: HTML 문서를 파싱하고, 원하는 데이터를 추출하는 데 사용
    1. Scrapy: 보다 고급의 웹 크롤러 프레임워크로, 비동기 작업을 지원하고 스케일업할 수 있는 기능을 제공
    1. Selenium: 자바스크립트로 동적으로 생성되는 콘텐츠를 처리할 때 사용
    1. Playwright: 자바스크립트로 동적으로 생성되는 콘텐츠를 처리할 때 사용 (Selenium의 대안)
        - 빠르고, 다양한 브라우저를 지원
        - 비동기 작업을 통해 효율적으로 동적 페이지를 크롤링
        - 최신 웹 애플리케이션과의 호환성이 뛰어남

1. 특징
    1. 파이썬은 상대적으로 직관적이고, 다양한 라이브러리가 제공되어 개발이 빠름
    1. BeautifulSoup이나 Scrapy를 사용하여 복잡한 웹 크롤링도 쉽게 처리할 수 있음
    1. 비동기 처리가 필요할 경우 asyncio나 aiohttp를 활용할 수 있음

## with java
1. 주요 도구 및 라이브러리
    1. Jsoup: 자바에서 HTML을 파싱하고, 데이터를 추출하는 데 사용되는 라이브러리, 파이썬의 BeautifulSoup과 비슷한 역할
    1. HttpClient: HTTP 요청을 보내는 데 사용, 자바에서는 HttpURLConnection 또는 Apache HttpClient를 사용
    1. Selenium: 자바에서도 Selenium을 사용할 수 있으며, 자바스크립트로 동적으로 생성되는 페이지를 처리하는 데 유용

1. 특징
    1. 자바는 멀티스레딩을 지원하므로 대규모 크롤링 작업에서 성능을 최적화할 수 있음
    1. Jsoup은 HTML 파싱과 데이터 추출에 매우 강력하고, 파이썬의 BeautifulSoup보다 더 높은 성능을 자랑
    1. 자바에서는 HttpClient를 사용하여 HTTP 요청을 보낼 수 있음, 이는 고급 옵션을 제공하지만 설정이 파이썬보다 다소 복잡
    1. 자바는 동기화 및 멀티스레딩을 활용하여 대규모 데이터 크롤링을 할 때 유리할 수 있음

## python vs java
|항목|python|java|
|---|---|---|
|개발 속도|빠름|다소 느림|
|라이브러리 지원|Requests, BeautifulSoup, Scrapy 등|Jsoup, HttpClient 등이 있지만, 설정이 복잡|
|비동기 처리|asyncio와 aiohttp 사용가능|CompletableFuture 등을 사용|
|성능|적당(작은 프로젝트에 적합)|높음(대규모 크롤링에 적합)|
|멀티스레딩|지원하지만 자바에 비해 불편|멀티스레딩을 통해 높은 성능을 가능|

- python은 빠르게 개발하고 실험해 볼 수 있는 환경을 제공, 간단한 크롤링이나 동적 페이지 크롤링을 할 때 유리
- java는 대규모 크롤링이나 성능이 중요한 경우에 더 적합, 멀티스레딩 및 고급 설정을 통해 더 많은 데이터를 효율적으로 처리 가능

## 관련 지식

### DOM
- Document Object Model
- 웹페이지의 구조를 트리 형태로 표현한 표준화된 모델
- 브라우저가 HTML 문서를 읽으면, 그 문서를 **태그 하나하나 객체(Object)** 로 변환해서 트리 구조로 만듬
- HTML 코드를 브라우저가 이해할 수 있는 구조화된 객체들로 바꾼 것
- 브라우저가 HTML을 해석해 만든 트리 구조의 문서 모델
- 예시
    - HTML 코드
    ```
    <html>
        <body>
            <h1>Hello</h1>
            <p>World</p>
        </body>
    </html>
    ```
    - DOM
        - 브라우저 내부의 트리모델
        - 각 태그는 “노드(node)” 라고 불리고, 서로 부모/자식 관계를 가짐
    ```
    Document
    └── html
        └── body
            ├── h1 ("Hello")
            └── p ("World")
    ```
- 웹 크롤러에서 DOM이 중요한 이유
    - 원하는 요소를 찾을 때 DOM 구조를 기준으로 찾음
        - BeautifulSoup: find(), select()
        - Selenium: find_element(By.CSS_SELECTOR, ...)
    - CSS Selector, XPath 등이 모두 DOM 기반
    - 자바스크립트로 변경된 내용도 DOM에 반영되므로, 실시간 상태를 읽을 수 있음(Selenium)