
from flask import Response, request
from database.models import Book
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import Book, User
from flask_jwt_extended import jwt_required, get_jwt_identity

class BooksApi(Resource):
  @jwt_required
  def get(self):
    books = Book.objects().to_json()
    return Response(books, mimetype="application/json", status=200)

  @jwt_required
  def post(self):
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.objects.get(id=user_id)
    book = Book(**body, added_by=user)
    book.save()
    user.update(push__books=book)
    user.save()
    id = book.id
    return {'id': str(id)}, 200
 
class BookApi(Resource):
  @jwt_required
  def put(self, id):
    user_id = get_jwt_identity()
    book = Book.objects.get(id=id, added_by=user_id)
    body = request.get_json()
    Book.objects.get(id=id).update(**body)
    return '', 200
 
  @jwt_required
  def delete(self, id):
    user_id = get_jwt_identity()
    book = Book.objects.get(id=id, added_by=user_id)
    book.delete()
    book = Book.objects.get(id=id).delete()
    return '', 200
    
  @jwt_required
  def get(self, id):
    books = Book.objects.get(id=id).to_json()
    return Response(books, mimetype="application/json", status=200)
