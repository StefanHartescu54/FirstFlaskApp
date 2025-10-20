from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

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
    }
})

api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Make sure Flask listens on all interfaces