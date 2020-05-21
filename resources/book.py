
from flask import Response, request
from database.models import Book
from flask_restful import Resource

class BooksApi(Resource):
  def get(self):
    books = Book.objects().to_json()
    return Response(books, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    book = Book(**body).save()
    id = book.id
    return {'id': str(id)}, 200
 
class BookApi(Resource):
  def put(self, id):
    body = request.get_json()
    Book.objects.get(id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    book = Book.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    books = Book.objects.get(id=id).to_json()
    return Response(books, mimetype="application/json", status=200)
