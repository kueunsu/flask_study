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

if __name__ == '__main__':
    app.run(debug=True)

