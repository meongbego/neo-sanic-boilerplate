from sanic import Sanic
from .configs import Config
from sanic_cors import CORS
from sanic.response import json

# app = Sanic(__name__)

# @app.route("/")
# async def index():
#     return json("Welcome")


# if __name__ == '__main__':
#     app.run()

def create_app():
    app = Sanic(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .controllers import api_blueprint

    app.register_blueprint(api_blueprint)
    return app

