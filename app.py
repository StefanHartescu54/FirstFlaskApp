from flask import Flask
from flask_smorest import Api
import os

from db import db
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app(db_url = None):
    app = Flask(__name__)


    app.config.update({
        "PROPAGATE_EXCEPTIONS": True,
        "API_TITLE": "Stores REST API",
        "API_VERSION": "v1",
        "OPENAPI_VERSION": "3.0.3",
        "OPENAPI_URL_PREFIX": "/",
        "OPENAPI_SWAGGER_UI_PATH": "/swagger-ui",  # Changed from prefix to path
        "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
        "OPENAPI_SWAGGER_UI_CONFIG": {
            "displayRequestDuration": True,
            "tryItOutEnabled": True
        },
        "SQLALCHEMY_DATABASE_URI" : db_url or os.getenv("DATABASE_URL","sqlite:///data.db"),
        "SQLALCHEMY_TRACK_MODIFICATIONS" : False
    })

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app