from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app