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

# GET
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

#POST
@app.route('/books', methods = ['POST'])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    
    if not title or not author:
        return jsonify({"error" : "title과 author은 필수입니다"}),400
    
    new_id = books[-1]["id"]+1 if books else 1
    new_book = {"id" : new_id, "title" : title, "author" : author}
    books.append(new_book)
    
    return jsonify(new_book),201


#PUT
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

#DELETE
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message" : f"{book_id}번 책이 사라졌습니다"})
    return jsonify({"error" : f"{book_id}번 책을 찾을 수 없습니다"}),404

if __name__ == '__main__':
    app.run(debug=True)