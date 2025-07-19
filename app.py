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

