from hello import img_deal
from flask import Flask
from img_api.__init__ import create_img_api

DEFAULT_APP_NAME = 'rb3d'


def create_app():
    app = Flask(DEFAULT_APP_NAME)
    app.register_blueprint(img_deal, url_prefix="/img_deal")

    create_img_api(app)

    return app
