from flask import Flask

app = Flask(__name__)

@app.route('/')
def book():
    return {'hello': 'world'}


app.run()