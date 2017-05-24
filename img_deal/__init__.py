from hello import img_deal
from user import user
from flask import Flask
from img_api.__init__ import create_img_api
from celery import Celery
from settings import config

DEFAULT_APP_NAME = 'rb3d'


def create_app(package_name, package_path, settings_override=None, celery_app=False):
    app = Flask(DEFAULT_APP_NAME)
    app.register_blueprint(img_deal, url_prefix="/img_deal")
    app.register_blueprint(user, url_prefix="/img_deal")

    create_img_api(app)

    return app


def create_celery_app(app=None):
    app = app or create_app('app', ['app'], celery_app=True)

    celery = Celery(__name__, broker=config.CELERY_BROKER_HOST, backend=config.CELERY_BACKEND_HOST)

    celery.conf.update(app.config)
    #
    # TaskBase = celery.Task
    #
    # class ContextTask(TaskBase):
    #     abstract = True
    #
    #     def __call__(self, *args, **kwargs):
    #         with app.app_context():
    #             return TaskBase.__call__(self, *args, **kwargs)
    #
    # celery.Task = ContextTask
    #
    return celery
