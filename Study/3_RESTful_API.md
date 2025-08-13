- step3 - RESTful API
### RESTful API

**API**

- 프로그램끼리의 대화를 도와주는 통로
- 컴퓨터가 GET /user?name=슈 이런식으로 요청을 보내면 서버는 JSON 형태로 데이터 보내줌
- 즉 API는 프로그램끼리 요청과 응답을 주고받는 약속된 방법

**RESTful**

- API를 만드는 규칙, 철학
    
    
    | 기능 | RESTful한 URL 예시 | 의미 |
    | --- | --- | --- |
    | 유저 목록 확인 | `GET /users` | 유저 목록 요청 |
    | 유저 한명 보기 | `GET /users/1` | ID 1번 유저 요청 |
    | 유저 생성 | `POST /users` | 유저 생성 요청 |
    | 유저 수정 | `PUT /users/1` | 1번 유저 수정 |
    | 유저 삭제 | `DELETE /users/1` | 1번 유저 삭제 |
- 이렇게 HTTP 메서드(GET, POST 등)와 URL 구조를 의미있게 조합하는 것을 RESTful하다 함
- RESTful은 단순히 관습이 아니라 잘 읽히는 API를 만드는 원칙

**CRUD**

- Create, Read, Update, Delete
- 생성, 조회, 수정, 삭제를 의미하는 API의 가장 기본적인 4가지 기능

**경로 파라미터 vs 쿼리 파라미터**

| 종류 | 예시 | Flask에서 받는 법 | 설명 |
| --- | --- | --- | --- |
| 경로 파라미터 | /user/username | @app.route(’/user/<username>’)
+ def func(username) | 경로 일부가 변수처럼 처리 |
| 쿼리 파라미터 | /user?name=eunsu | request.args.get(’name’) | URL 뒤에 붙어서
Key=value 형태로 전달 |
- REST에서는 **URL = 자원의 경로**라고 각
    
    → 즉, `user`라는 자원 안의 `"은수"`라는 개별 항목을 요청하는 건 `/user/은수`처럼 쓰는 게 더 자연스러움
    
     쉽게 말하면:
    
    - `?name=은수`는 값을 전달하는 "질문 방식"
    - `/user/은수`는 파일 경로처럼 "자원에 접근하는 방식"
- 쿼리 파라미터는 **“선택적 조건이나 필터를 줄 때”** 강력함
    - ex) products?category=책&sort=price_desc → 책 카테고리만 보되, 가격을 내림차순으로 정렬
    - ex) posts?search=파이썬 → 파이썬 관련 게시글만 검색
- 경로 파라미터는 **“정해진 자원을 직접 지정할 때”** 강력함
    - ex) /user/1 → 1번 유저의 정보를 가져와!
    - ex) /posts/15/comments → 15번 게시물의 댓글을 가져와!
    - ex) /fils/logo.png → logo.png 파일 요청
- 경로 파라미터는 필수값, 쿼리 파라미터는 선택적 조건이라는 성격이 강함