- step4 - CRUD
    
    **GET - Read**
    
    <aside>
    
    url에 author를 입력함으로써 입력한 author에 해당하는 책의 제목을 가져오는 구문
    
    입력하는 url : http://127.0.0.1:5000/books/은수
    
    실제 로컬 서버 url에 입력해 결과를 확인할 수 있음 → GET만 가능 유일!!
    (다른 POST, PUT, DELETE는 postman이나 curl을 통해 결과를 확인 가능함)
    
    ```python
    @app.route('/books/<string:book_author>',methods=['GET'])
    # <string:book_author>에서 url에 들어가는 경로 파라미터 값이 book_author에 들어감
    def get_books_by_author(book_author):
        result = [book["title"] for book in books if book["author"] == book_author]
        return jsonify(result)
    ```
    
    ```python
    1.
    @app.route('/books/<string:book_author>',methods=['GET'])
    # <string:book_author>에서 url에 들어가는 경로 파라미터 값이 book_author에 들어감
    ```
    
    ```python
    2.
    def get_books_by_author(book_author):
    # 쿼리 파라미터와는 달리 request.args.get으로 url에 입력된 값을 받아오지 않음
    # url 선언에 사용한 변수값을 함수의 입력 파라미터 값으로 전달하면
    # url에 입력된 경로 파라미터 값을 함수 내에서 사용 가능
        result = [book["title"] for book in books if book["author"] == book_author]
        # books list에 입력된 author와 같은 author만 뽑아 새로운 result를 생성
        return jsonify(result)
    ```
    
    </aside>
    
    **POST - Create**
    
    <aside>
    
    이미 존재하는 책 리스트에 추가 리스트 항목을 만들어 추가하기
    
    ```python
    @app.route('/books', methods=['POST'])
    def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    if not title or not author:
        return jsonify({"error": "title과 author는 필수입니다"}), 400
    
    new_id = books[-1]['id'] + 1 if books else 1
    new_book = {"id": new_id, "title": title, "author": author}
    books.append(new_book)
    
    return jsonify(new_book), 201
    ```
    
    - postman에서 body값에 넣고싶은 data를 입력
    - { “title” : “은수의 자서전”, “author” : “은수”}
        
        → 실제로 books에 추가된 것을 알 수 있음
        
    </aside>
    
    **PUT - Update**
    
    <aside>
    
    내가 수정하고 싶은 데이터를 입력해 원래의 값에서 입력한 값으로 업데이트 하고자 함
    
    ```json
    입력하는 새로운 데이터 예시
    {
    	"title" : "수정된 책 내용",
    	"author" : "수정된 저자 이름"
    }
    ```
    
    ```python
    @app.route('/books/<int:book_id>',methods=['PUT'])
    def update_book(book_id):
        data = request.get_json()
        new_title = data.get("title")
        new_author = data.get("author")
        
        if not new_author or not new_title:
            return jsonify({"error" : "title과 author은 필수 입력값입니다"}),400
        
        for book in books:
            if book["id"] == book_id:
                book["title"] = new_title
                book["author"] = new_author
                return jsonify(book)
        return jsonify({"error" : "일치하는 ID가 존재하지 않습니다"}),404
    ```
    
    - 경로 파라미터로 수정하고 싶은 책의  id를 받음
    - 수정하고 싶은 내용을 JSON으로 받고 title, author에 관한 정보를 `data.get`으로 뽑아냄
    - id에 해당하는 책을 찾아 내용으 수정
    </aside>
    
    **DELETE - delete**
    
    <aside>
    
    삭제하고 싶은 책의 id를 입력해 삭제하는 구문
    
    ```python
    @app.route('/books/<int:book_id>',methods=['DELETE'])
    def delete_book(book_id):
        
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                return jsonify({"message" : f"{book_id}번 책이 사라졌습니다"})
        return jsonify({"error" : f"{book_id}번 책을 찾을 수 없습니다"}),404
    ```
    
    - 삭제만 하는 구문이므로 입력받는 값은 없음
    - delete와 유사함 → id를 비교해 해당 id의 책을 제거
    </aside>
    
    **CURL**
    
    - 로컬 서버나 postman 없이도 결과를 테스트해볼 수 있는 방법
    - 기본 구성 : `curl -X [method] [URL]`
        - GET 요청은 기본값이라 -X GET을 생략가능함
        - 터미널에 `curl http://localhost:5000/books` 과 같이 적어주면 JSON 형식의 결과가 출력됨
        - 다른 method는 `curl -X POST http://localhost:5000/books` 과 같이 써주어야 함
        - 뒤에 `|jq` 를 붙이면 알아보기 쉬운 문자열로 확인가능함
        
        | 옵션 | 설명 |
        | --- | --- |
        | `-X` | 메서드 지정 (GET, POST, PUT, DELETE 등) |
        | `-H` | 헤더 설정 (예: `Content-Type`) |
        | `-d` | 전송할 데이터 (JSON 문자열 등) |
        | `-i` | 응답 헤더도 같이 보기 |
        | `-v` | verbose 모드 (요청/응답 전체 보기) |
    - POST와 PUT과 같은 method는 데이터도 함께 전송해야 함
        - `-d '{"title":"은수의 자서전", "author":"은수"}’`과 같이 추가적인 데이터도 함께 적어줘야 함
        - 작은 따옴표로 JSON 전체를 감싸고 내부는 큰 따옴표로 키와 값을 감싸는 것이 규칙
    - 헤더는 ‘이 요청이 어떤 형식의 데이터인지’ 서버에게 알려주는 역할을 함
        - `-H "Content-Type: application/json”` 과 같은 형식으로 전송됨
        - 이는 보내는 데이터가 JSON 형식이라는 의미임
        - REST API에서는 거의 항상 이렇게 써줌