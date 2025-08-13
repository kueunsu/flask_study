from flask import Flask, request, jsonify

app = Flask(__name__)
'''
What is CRUD
POST - Create
GET - Read
PUT - Update
DELETE - Delete
'''

books = [
    {"id": 1, "title": "파이썬 기초", "author": "윤미"},
    {"id": 2, "title": "백엔드 입문", "author": "은수"},
    {"id": 3, "title": "flask 실전", "author": "윤미"},
    {"id": 4, "title": "연애 실전", "author": "추진"}
]

@app.route('/books/<string:book_author>',methods=['GET'])
def get_books_by_author(book_author):
    result = [book["title"] for book in books if book["author"] == book_author]
    return jsonify(result)

@app.route('/books/<int:book_id>',methods=['GET'])
def get_books_by_id(book_id):
    result = [book["title"] for book in books if book["id"] == book_id]
    return jsonify(result)

@app.route('/books',methods=['GET'])
def get_books_if_no_input():
    return ('there is no input. please enter id or author')

if __name__ == '__main__':
    app.run(debug=True)