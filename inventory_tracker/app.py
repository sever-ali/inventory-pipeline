from flask import Flask
from app.routes import main
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    app.register_blueprint(main)

    return app
