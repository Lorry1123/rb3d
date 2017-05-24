# coding: utf8

import datetime
import hashlib
import requests

from app.tasks import send

from settings import SenderAlidayuConfig
from .base import SMSSenderBase


class AliDayuSender(SMSSenderBase, SenderAlidayuConfig):

    def __init__(self):
        super(AliDayuSender, self).__init__()

        self.default_common_params = dict(
            method=self.API_NAME,
            app_key=self.APP_KEY,
            sign_method='md5',
            timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            format='json',
            v='2.0'
        )
        self.default_send_params = dict(
            sms_type='normal'
        )

    @staticmethod
    def fill_send_params(tpl_id, tpl_value, mobile, sign_name):
        ret = dict(
            # single send params
            sms_template_code=tpl_id,
            sms_param=tpl_value,
            rec_num=mobile,
            sms_free_sign_name=sign_name,
        )

        return ret

    def data_maker(self, tpl_id, tpl_value, mobile, uid, buyer_nick, sign_name):
        # fill common params
        params = self.default_common_params

        # fill send params
        params.update(self.default_send_params)
        params.update(AliDayuSender.fill_send_params(tpl_id, tpl_value, mobile, sign_name))

        params.update(dict(extend=uid))
        # get sign by md5
        sign = self.sign(params)
        params['sign'] = sign

        return params

    def sign(self, params):
        params = "%s%s%s" % (self.APP_SEC,
                             ''.join('%s%s' % (k, v) for k, v in sorted(params.items())),
                             self.APP_SEC)

        sign = hashlib.md5(params).hexdigest().upper()

        return sign

    def send_msg(self, data, url=None):
        url = url or self.API_URL
        _id = send.send_msg.delay(data, url).id

        return 'send task built', _id

    def query(self, mobile, date):
        # TODO: separate fill params function
        params = self.default_common_params
        params.update({'rec_num': mobile, 'query_date': date, 'current_page': 1, 'page_size': 50})
        params['method'] = 'alibaba.aliqin.fc.sms.num.query'

        sign = self.sign(params)
        params['sign'] = sign

        r = requests.post(self.API_URL, params)

        print r.text

    # def check_response(self, r):
    #     if r.find('error_response') >= 0:
    #         return 0
    #     else:
    #         return 1

    def get_msg_detail(self):
        # TODO: 开发者平台中订阅消息，才能拿到短信的具体回执，这里可能需要搞一搞, 数据也需要本地保存

        params = self.default_common_params
        params['method'] = 'taobao.tmc.messages.consume'
        params['sign'] = self.sign(params)

        r = requests.post(self.API_URL, params)

        return r.text
