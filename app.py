from flask import Flask, Request, Response
from database.db import initialize_db
from database.models import Book
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/book-db'
}

initialize_db(app)

initialize_routes(api)
app.run()