class Config(object):
    MONGODB_HOST = "mongodb://127.0.0.1:27017/"
    MONGODB_NAME = "rb3d"

    REDIS_BASE_HOST = "redis://127.0.0.1:6379/"
    REDIS_HOST = REDIS_BASE_HOST + '6'
    REDIS_SESSION_PREFIX = 'session:'

    CELERY_BROKER_HOST = REDIS_BASE_HOST + '7'
    CELERY_BACKEND_HOST = REDIS_BASE_HOST + '8'

config = None

if not config:
    config = Config
