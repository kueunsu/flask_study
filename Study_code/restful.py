from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "author": "윤미"},
    {"id": 2, "title": "백엔드 입문", "author": "은수"},
    {"id": 3, "title": "flask 실전", "author": "윤미"},
    {"id": 4, "title": "연애 실전", "author": "추진"}
]

@app.route('/books',methods=['GET'])
def get_books_by_author():
    author = request.args.get('author')
    if author:
        result 
    return 

@app.route('/books/<int:book_id>',methods=['GET'])
def get_books_by_id():
    return 