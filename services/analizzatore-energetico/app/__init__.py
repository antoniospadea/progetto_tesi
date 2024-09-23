from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importiamo e registriamo le route dall'API principale (main.py)
    from .main import api
    app.register_blueprint(api)

    return app

