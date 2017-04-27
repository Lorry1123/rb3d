class Config(object):
    MONGODB_HOST = "mongodb://127.0.0.1:27017/"
    MONGODB_NAME = "rb3d"

config = None

if not config:
    config = Config
