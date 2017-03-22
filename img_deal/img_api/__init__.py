from .test_api import test
from flask import Flask


def create_img_api(app):
    app.register_blueprint(test, url_prefix="/img_api")

