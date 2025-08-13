from flask import Flask, jsonify, request

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

@app.route('/api/greet',methods=['POST'])
def api_greet():
    data = request.get_json()
    name = data.get('name','익명')
    message = f'안녕하세요!! {name}님~~'
    return jsonify({'message':message})

@app.route('/api/user',methods=['GET'])
def get_user_info():
    username = request.args.get('name')
    if username:   
        return jsonify({'message' : f'User is {username}'})
    else:
        return jsonify({'error':'No name providedr'}),400
    
@app.route('/api/add', methods=['GET'])
def add_func():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) + int(b)
    except(ValueError, TypeError):
        return jsonify({'error' : '숫자를 보내주세요'}),400
    return jsonify({'result' : result})

if __name__ == '__main__':
    app.run(debug=True)

