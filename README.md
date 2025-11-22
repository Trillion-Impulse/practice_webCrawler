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

### HTTP Request
- HTTP 요청
- 클라이언트(브라우저, 앱, 크롤러)가 서버에게 리소스나 작업을 요청할 때 보내는 메시지
- 웹에서 이루어지는 모든 데이터 통신의 기본 단위이며, HTTP 프로토콜을 구성하는 요소 중 하나
- HTTP Request의 구성 요소
    1. Request Line (요청 시작줄)
        - 요청의 목적을 나타내는 한 줄
            ```
            GET /index.html HTTP/1.1
            ```
            - HTTP Method: GET, POST, PUT, DELETE, PATCH …
            - Request Target: 요청할 경로(/index.html)
            - HTTP Version: HTTP/1.1, HTTP/2 등                     
    1. Request Headers (요청 헤더)
        - 요청에 대한 부가 정보를 전달하는 필드
            ```
            Host: example.com
            User-Agent: Mozilla/5.0 ...
            Accept: text/html
            Accept-Language: ko-KR
            Authorization: Bearer xxx...
            ```
        - 헤더의 역할
            - 클라이언트 정보를 서버에 전달 (User-Agent, Referer 등)
            - 인증 정보 제공 (Authorization)
            - 원하는 데이터 종류 지정 (Accept)
            - 언어, 인코딩, 쿠키 등 상태 정보 제공
    1. Request Body (요청 본문, 선택적)
        - 데이터가 필요한 요청에서만 추가됨
        - GET은 보통 없음, POST/PUT/PATCH 등의 요청에서 사용
            ```
            {
                "username": "test",
                "password": "1234"
            }
            ```
- HTTP Request의 동작 과정 (간단 흐름)
    1. 클라이언트가 URL로 서버에 요청 Request를 보냄
    1. 요청은 TCP/IP를 통해 서버로 전달됨
    1. 서버는 요청을 분석하고 처리
    1. 그 결과를 HTTP Response로 다시 클라이언트에게 전송
    1. 클라이언트는 응답을 화면에 렌더링하거나 데이터를 처리
- 크롤링 관점에서 본 HTTP Request
    - 웹 크롤러는 브라우저처럼 보이기 위해 HTTP Request를 직접 구성하여 서버에 요청을 보내는 프로그램
    - 따라서 HTTP Request를 이해하는 것은 크롤링의 핵심 기술
    - HTTP Request가 크롤링에서 중요한 이유
        1. 브라우저 대신 “프로그래밍 방식”으로 요청을 보내야 함
            - 크롤러는 HTML 페이지, API 응답, 이미지, JSON 데이터 등을 얻기 위해 직접 HTTP Request를 생성해 서버에 보내야 한다.
        1. 서버는 요청 헤더를 분석해 크롤러를 차단하기도 함
            - 특정 헤더(User-Agent, Referer, Cookie 등)가 없으면, 봇으로 판단해 접속을 막는 경우가 많다.
        1. 올바른 요청을 보내야 원하는 데이터가 받아짐
            - 예를 들어로그인 후 데이터는 쿠키나 토큰이 필요함 → Request Header 완성도가 요구됨
    - 크롤러가 구성해야 하는 HTTP Request의 핵심 요소
        1. Method (요청 방식)
            - GET : HTML, JSON 등 조회
            - POST : 로그인, 검색, 폼 제출
            - PUT/PATCH/DELETE : 대부분 관리용 API
            - 크롤링에서는 GET + POST 조합이 거의 전부
        1. Headers (가장 중요!)
            - 크롤링 시 필수 또는 매우 중요한 헤더
                | 헤더                  | 역할                            |
                | ------------------- | ----------------------------- |
                | **User-Agent**      | 브라우저/봇 정보. 크롤링 차단 회피 핵심       |
                | **Referer**         | 이전 페이지 정보. 없으면 막는 사이트 있음      |
                | **Cookie**          | 로그인/세션 정보 유지                  |
                | **Accept**          | 원하는 응답 타입 지정 (HTML/JSON 등)    |
                | **Accept-Language** | 언어 설정                         |
                | **Authorization**   | JWT, Bearer Token 등 인증 API 접근 |
            - User-Agent + Cookie + Referer 조합은 많은 사이트에서 사람이 접속했다고 판단하는 최소 조건
        1. Body (POST 요청 시 사용)
            - 로그인, 검색, 필터 적용 등에 필요
                ```
                {
                    "keyword": "python",
                    "page": 1
                }
                ```
    - 크롤러가 실제로 HTTP Request를 쓰는 방식
        - Requests 기반 크롤러
            - 직접 요청 구성 → 서버는 봇으로 오인할 가능성 높음 → 따라서 헤더를 신경 써서 “브라우저처럼” 구성해야 함
        - Selenium 기반 크롤러
            - 실제 브라우저가 HTTP Request를 전송하므로 일반적인 Request Headers는 자동으로 채워짐
            - 필요할 때만 User-Agent나 쿠키를 수정함
    - 크롤링에서 HTTP Request와 관련된 주요 문제들
        | 문제               | 원인                        | 해결                             |
        | ---------------- | ------------------------- | ------------------------------ |
        | 403 Forbidden    | User-Agent 없음, Referer 없음 | 적절한 헤더 추가                      |
        | 로그인 유지 안 됨       | Cookie 누락                 | 세션 유지 + 쿠키 전송                  |
        | API 호출 실패        | Authorization 누락          | 토큰 발급 후 Header에 포함             |
        | 모바일/PC 페이지 다르게 뜸 | User-Agent 영향             | 모바일 UA/데스크탑 UA 설정              |
        | 계속 리디렉션          | CSRF 토큰 없음                | Request Body + Header에 CSRF 포함 |
    - 크롤링 관점에서 HTTP Request 전체 구조 요약
        ```
        HTTP Request
        ├── Method        ← GET / POST 요청의 종류
        ├── URL           ← 요청할 주소
        ├── Headers       ← User-Agent / Cookie / Referer / Accept …
        ├── Body          ← POST/PUT에서 사용하는 데이터
        └── Session/Cookie← 로그인 유지 시 필요
        ```

### BeautifulSoup

#### find vs select 비교
- find / find_all
    - BeautifulSoup가 제공하는 태그 이름 + 속성 기반 탐색
- select / select_one (CSS 선택자)
    - 웹 개발에서 사용하는 CSS selector 문법 그대로 사용
- 비교 표
    | 비교 항목 | `find` / `find_all` | `select` / `select_one` (CSS Selector) |
    |----------|----------------------|-----------------------------------------|
    | **기본 개념** | 태그명 + 속성 기반 탐색 | CSS 선택자 기반 탐색 |
    | **표현력** | 보통 (단순 구조에 적합) | 매우 높음 (복잡한 DOM도 쉽게 표현) |
    | **사용 예시** | `soup.find("div", class_="title")` | `soup.select_one("div.title")` |
    | **후손/자식 탐색** | 비표준적 / 번거로움 | `div > p`, `div p`로 직관적 표현 가능 |
    | **class 여러 개 탐색** | 불편함 (`class_=["a", "b"]` 등) | `.a.b`로 간단하게 표현 |
    | **id 탐색** | `find(id="main")` | `#main`으로 간단 |
    | **복잡한 조건 처리** | 어려움 | 매우 유리 |
    | **코드 가독성** | 단순한 구조에서는 최고 | 복잡한 구조 파싱에 최고 |
    | **유지보수성** | HTML 구조 변경에 약함 | 구조가 바뀌어도 대응하기 쉬움 |
    | **속도** | 빠름 (상대적으로 빠른 편) | 약간 느림 (CSS 파싱 필요) |
    | **추천 사용 상황** | 단순한 태그/구조 | 복잡한 DOM, class 다수, 구조적 탐색 필요 |
    | **실전 활용도** | 중간 ~ 높음 | 매우 높음 |
- 단순/정적 구조 → `find`
- 복잡한 HTML, class가 많거나 구조 기반 탐색 필요 → `select`
- 실제 프로젝트에서는 두 방식을 혼합해서 사용하는 것이 가장 효율적


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

### 네이버 뉴스 AJAX 역공학 방식 크롤링 시도 실패 기록
- AJAX 요청에서 확인해야 하는 요소
    - Request URL: 요청을 보내는 엔드포인트 주소
    - Query String Parameters (qs): 요청 시 전달되는 파라미터 (검색어, 페이지 번호, 정렬 등)
    - Headers
    - User-Agent: 브라우저 환경 흉내
    - Referer: 요청이 발생한 페이지
    - X-Requested-With: XMLHttpRequest 여부
    - 기타 서버에서 요구하는 인증/보안 헤더
    - Cookies: 세션 관리나 로그인 정보, 브라우저에서 생성되는 특정 쿠키
    - Response
    - 정상적으로 JSON 데이터가 오는지
    - JSON 내부에 HTML fragment가 포함되어 있는지
    - HTML fragment 내에서 필요한 데이터(뉴스 링크, 제목, 내용)를 추출할 수 있는 구조 확인
- 크롤러 코드 작성 시 고려할 사항
    - requests 모듈을 사용하여 GET/POST 요청을 보낼 수 있음
    - URL, Query Parameters, Headers, Cookies를 설정
    - 응답이 JSON이면 .json()으로 파싱, HTML fragment는 BeautifulSoup 등으로 파싱
    - 반드시 응답 상태 코드 확인 (response.status_code)
    - 응답 내용 길이 확인 → 빈 응답인지 확인 (len(response.text))
- AJAX 요청이 성공하기 위한 요청 조건
    - 서버가 요구하는 필수 헤더, 세션, 쿠키, 토큰이 모두 포함되어야 함
    - 브라우저에서 동적 생성되는 값(쿠키, CSRF 토큰 등)이 포함되어야 함
    - Referer, User-Agent 등이 실제 브라우저 환경과 유사해야 함
    - 그렇지 않으면 응답 길이 0 또는 JSON 파싱 실패 발생
    - 네이버 뉴스의 경우 단순 requests GET 요청만으로는 빈 응답이 돌아옴
- AJAX 역공학 방식 사용 기준
    | 구분            | 설명                                                                                                                      |
    | ------------- | ----------------------------------------------------------------------------------------------------------------------- |
    | **사용할 때**     | - 공식 API가 없고, 브라우저에서만 데이터가 로드됨<br>- 실험적으로 요청 구조를 확인하고 재현 가능할 때<br>- 소규모 테스트나 개인 프로젝트에서                                  |
    | **사용하지 않을 때** | - 공식 API가 존재하는 경우 → 안정적이고 효율적<br>- 대규모/상용 서비스에서 → IP 차단, 법적/윤리적 문제 위험<br>- 서버가 동적 토큰, 쿠키를 필수로 요구하는 경우 → 단순 requests로 불가 |
- 결론
    - AJAX 요청 역공학은 공식 API가 없는 경우의 최후 수단
    - 공식 API 사용이 가능하면 반드시 API 활용
    - 브라우저 환경을 완전히 재현하지 않으면 requests만으로는 실패 가능성이 높음
    - 크롤러 개발과 디버깅에 참고하기 위해 기록