from .db import db

class Book(db.Document):
    title = db.StringField(required=True, unique=True)
    author = db.StringField(required=True)
    language = db.StringField(required=True)
    year = db.IntField(required=True)
