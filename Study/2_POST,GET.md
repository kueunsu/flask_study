- step2 - GET / POST
    
    ### GET & POST
    
    <aside>
    
    🔸  웹에서 가장 기본적인 두 가지 요청 방식 - HTTP 메서드
    
    🔸  GET : 데이터 요청 ex) 웹페이지 보기, 뉴스 기사 보기
    
    🔸 POST : 데이터 전송 ex) 로그인 정보 전송, 댓글 작성, 회원 가입 등
    
    🔸 GET은 브라우저에서 주소창에 직접 쳐 들어가 확인할 수 있음
    
    🔸 반면 POST는 숨겨진 데이터이기 떄문에 웹 폼, Postman이나 JS 코드로만 보낼 수 있음
         → 따라서 POST로 만들어진 경로로 직접 들어가면 405 erorr 발생
         → 또한 일반적인 사용자는 웹 폼 input box를 통해 입력을 제출
    
    </aside>
    
    **예제코드**
    
    <aside>
    
    ```python
    @app.route('/api/greet', methods=['POST'])
    def greet():
        data = request.get_json()
        name = data.get('name', '익명')
        message = f'안녕하세요, {name}님!'
        return jsonify({'message': message})
    ```
    
    ---
    
    코드 정리
    
    ```python
    1. 
    @app.route('/api/greet', methods=['POST'])
    	# /api/greet 경로로 POST 요청을 보내면 아래 함수를 실행하라는 명령
    	# /api/greet 경로는 POST 요청만 받음
    	# 따라서 브라우저에서 직접 경로에 접근하면 에러가 발생
    ```
    
    ```python
    2. 	
    	# JSON : 데이터를 주고받기 위해 만든 아주 간단한 문자열 기반의 자료 형식
    	# { "키1" : "값1", "키2" : 20 } 형식 -> 파이썬의 딕셔너리와 매우 유사
    	# 이런 JSON 문자열을 딕셔너리로 변환해야 데이터를 사용 가능. 이를 "파싱"이라 함
    data = request.get_json()
    	# 입력받은 JSON을 딕셔너리로 변환하는 코드
    	# data는 내가 설정한 변수명, 나머지는 고정인 코드
    	# 이 코드의 결과로 입력받은 데이터가 딕셔너리 형태로 data에 저장됨
    name = data.get('name', '익명')
    	# 입력받은 데이터가 name이라는 키라 예상하고 name에 해당하는 변수에 값을 넣음
    	# 값이 오지않으면 기본값으로 '익명'이라는 값을 넣어줌
    ```
    
    ```python
    3.
    message = f'안녕하세요, {name}님!'
    	# 파이썬의 f-string 문법. 변수를 문자열안에 바로 넣을 수 있게 함
    return jsonify({'message': message})
    	# jsonify : 파이썬 딕셔너리를 JSON 문자열로 바꿔주는 Flask 함수
    	# 만든 메세지를 return을 통해 응답(response)으로 클라이언트에게 전달
    ```
    
    </aside>
    
    **postman에서 직접 데이터 입력해보고 확인하기**
    
    - postman - HTTP - POST  - http://127.0.0.1:5000/api/greet 경로 입력
    - Body - raw - JSON 선택
    - data 입력
        
        ```
        {
            "name" : "eunsu"
        }
        ------
        {
        }
        ```
        
    - 결과
        
        ```
        {
            "message": "안녕하세요!! eunsu님~~"
        }
        -------
        {
        		"message": "안녕하세요!! 익명님~~"
        }
        ```