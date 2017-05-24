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


class SenderYunpianConfig(object):
    APP_KEY = "44fb01a4a9f4aea703876e18606cbc5b"
    YINGXIAO_KEY = '6561c26d09de9c701f637836d8dcbebf'

    # msg api
    SINGLE_SEND_API_URL = "https://sms.yunpian.com/v2/sms/single_send.json"
    BATCH_SEND_API_URL = "https://sms.yunpian.com/v2/sms/batch_send.json"
    MULTI_SEND_API_URL = "https://sms.yunpian.com/v2/sms/multi_send.json"
    QUERY_BY_MOBILE_API_URL = "https://sms.yunpian.com/v2/sms/get_record.json"

    # sign api
    ADD_SIGN_API = 'https://sms.yunpian.com/v2/sign/add.json'
    QUERY_SIGN_API = 'https://sms.yunpian.com/v2/sign/get.json'

    # template api
    ADD_TEMPLATE_API = 'https://sms.yunpian.com/v2/tpl/add.json'
    QUERY_TEMPLATE_API = 'https://sms.yunpian.com/v2/tpl/get.json'

    # black words
    BLACK_WORDS_API = 'https://sms.yunpian.com/v2/sms/get_black_word.json'

    # consts
    MAX_SEND_SIZE = 1000