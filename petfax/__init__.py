# config
from flask import Flask

# factory


def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, Petfax!'

    # return the app
    return app
