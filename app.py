from flask import Flask, Request, Response
from database.db import initialize_db
from database.models import Book

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/book-db'
}

initialize_db(app)

@app.route('/books')
def get_books():
    books = Book.objects().to_json()
    return Response(books, mimetype="application/json", status=200)

@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
    book = book(**body).save()
    id = book.id
    return {'id': str(id)}, 200

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    body = request.get_json()
    book.objects.get(id=id).update(**body)
    return '', 200

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book.objects.get(id=id).delete()
    return '', 200

app.run()