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

### API
- Application Programming Interface
- 프로그램끼리 데이터를 주고받기 위해 만들어진 “통로” 또는 “규칙(명세)”
- 서버에게 데이터를 요청하는 공식적인 방법
- 프로그램끼리 서로 얘기할 때 쓰는 언어/규칙
- 응용 프로그램에서 사용할 수 있도록, 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
- 응용 프로그램에서 데이터를 주고받기 위한 방법
- 특징
    1. 사람이 아닌 프로그램이 읽기 좋게 되어 있다
        - HTML은 사람이 보는 화면 중심이라 파싱이 복잡하지만, API의 데이터는 컴퓨터가 읽기 쉽도록 JSON/XML로 제공
    1. URL로 요청하면 정확한 데이터만 반환한다
        - /news?page=1 → 1페이지 뉴스 데이터만
        - /product?id=1001 → 제품 상세 데이터만
    1. 공통 규칙이 있다
        - 대표적인 HTTP 메서드
            - GET (조회)
            - POST (전송)
            - PUT (수정)
            - DELETE (삭제)
    1. HTML 없이도 데이터를 가져올 수 있다
        - 그래서 API를 발견하면 Selenium도 BeautifulSoup도 필요 없음

### AJAX
- Asynchronous JavaScript And XML
- 웹페이지가 새로고침 없이 서버에서 데이터를 가져올 수 있게 해주는 기술
- 페이지 전체를 새로 불러오지 않고, 필요한 데이터만 서버에서 받아오는 기술
- 비교
    - 전통적인 웹페이지는 버튼을 클릭하면 페이지 전체가 새로 로딩
        ```
        [요청] → 전체 HTML 재로딩 → 화면 깜빡임 → 느림
        ```
    - AJAX 사용하면
        ```
        [요청] → 데이터(JSON)만 받아옴 → 화면만 일부 업데이트
        ```
- 특징
    - 빠름
    - 깜빡이지 않음
    - 부분 업데이트 가능
    - 사용자 경험 향상
- 네이버 뉴스, 유튜브, 인스타그램, 트위터 등의 무한스크롤은 모두 AJAX 기반
- 실제 동작 방식
    - AJAX는 다음 두 기술이 합쳐진 개념
        - JavaScript로 비동기 요청을 보냄
            - fetch(), XMLHttpRequest(XHR)
            - 브라우저가 알아서 서버에 요청을 보냄
        - 응답(JSON 등)을 받아 페이지 일부만 갱신
            - 데이터만 받아와 화면에 뿌리기
    - AJAX는 “언어”나 “API”가 아니라 비동기 방식으로 API를 호출하는 웹 기술
- AJAX는 결국 API를 부르는 기술이다
    - 예를 들어 아래와 같은 요청이 Network 탭에서 보이면, 브라우저가 JavaScript로 서버에 API 요청을 보내고 있는 것
        ```
        https://example.com/api/articles?page=3
        ```
    - 이게 바로 AJAX 요청 = 비공식 API 호출
- 그래서 크롤러는 예를 들어 아래와 같이 AJAX 기반 API를 직접 호출
    ```
    requests.get("https://example.com/api/articles?page=3").json()
    ```
    - 매우 빠름
    - 안정적
    - 정제된 JSON 데이터 바로 확보
    - 동적 페이지 크롤링을 위한 Selenium 같은 라이브러리 필요 없음
- API, AJAX, API 기반 크롤링의 관계
    | 개념             | 설명                                       |
    | -------------- | ---------------------------------------- |
    | **API**        | 서버가 데이터 전달을 위해 만든 공식/비공식 인터페이스           |
    | **AJAX**       | 브라우저가 JavaScript로 API를 비동기로 호출하는 기술      |
    | **API 기반 크롤링** | AJAX 요청을 Python에서 `requests`로 직접 호출하는 방식 |
- AJAX는 웹페이지가 새로고침 없이 서버의 API로부터 데이터(JSON)를 받아오는 기술이며,
    - AJAX 요청을 그대로 Python에서 호출하면 그것이 바로 API 기반 크롤링이다.