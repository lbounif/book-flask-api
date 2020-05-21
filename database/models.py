from .db import db

class Book(db.Document):
    title = db.StringField(required=True, unique=True)
    author = db.StringField(required=True, unique=True)
    language = db.IntField(required=True, unique=True)
    pages = db.ListField(db.StringField(), required=True)
