- step1 - 서버구성
    - 흐름
        1. 가상환경 만들기 → 프로젝트 별 충돌을 피하기 위해 독립적인 공간 할당
        2. 가상환경 활성화
        3. flask 설치
        4. flask 앱 파일 만들기 → app.py파일 생성
        5. 코드 작성 후 실행 → app.py 파일에 실행하고자 하는 코드를 작성하고 실행
            
            내가 작성한 코드 
            
            ```python
            from flask import Flask
            
            app = Flask(__name__)
            
            @app.route('/')
            def home():
                return 'Hello, 슈의 Flask 서버!'
            
            if __name__ == '__main__':
                app.run(debug=True)
            ```
            
            결과 : 브라우저에 내가 원하는 문구를 띄울 수 있음
            
            ![image.png](attachment:9e671443-30be-4527-9a1b-59c8a6403c66:image.png)
            
            - 127.0.0.1 : 내 컴퓨터의 IP를 나타냄 → 로컬 서버
            - :5000 → 포트번호(flask의 default 포트 번호)
    - flask
        - flask : 파이썬으로 웹 서버를 아주 간단하게 만들 수 있게 해주는 도구(프레임워크)
        - 웹 서비스 : 주소창에 ping을 받아서 서버가 응답을 돌려주는 것
        - flask는 그 요청 - 응답 과정을 파이썬 코드로 아주 쉽게 짤 수 있도록 도와줌
        - flask는 쉽고 빠르고 유연함
    - 코드 기본 구성
        
        ```python
        from flask import ...
        
        app = Flask(__name__) -> app이 서버의 이름이 됨
        
        @app.route('/경로')
        def 함수명():
        	return 실행하고자 하는 내용(출력하고싶은 내용 등..)
        
        if __name__ == '__main__': # 파일을 직접 실행할 때만 서버를 킴
        	app.run(debug=True) # debug=True는 코드 수정시 서버가 재시작
        ```
        
    - app.py 확장
        
        ```python
        from flask import Flask, jsonify
        
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            return 'Hello, 슈의 Flask 서버!'
        
        @app.route('/hello')
        def hello():
            return '안녕 슈! 여긴 /hello 엔드포인트야.'
        
        @app.route('/api/data')
        def api_data():
            data = {'name': '슈', 'project': '2025 서머 프로젝트'}
            return jsonify(data)
        
        if __name__ == '__main__':
            app.run(debug=True)
        ```
        
        결과 : / 뒤에 입력하는 값에 따라 추가적인 페이지 구성