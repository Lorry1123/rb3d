# coding: utf8
import requests

from settings import SenderYunpianConfig as config


def send(mobile, text):
    url = config.SINGLE_SEND_API_URL
    data = {
        'apikey': config.APP_KEY,
        'mobile': mobile,
        'text': text
    }

    print data

    resp = requests.post(url, data)
    print 'msg sent-----'
    print resp.text

