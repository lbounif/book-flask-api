from .db import db

class Book(db.Docuemnt){
    title = db.StringField(required=True, unique=True)
    author = db.StringField(db.StringField(), required=True)
    language = db.IntField(db.IntField(), required=True)
    pages = db.ListField(db.StringField(), required=True)
}