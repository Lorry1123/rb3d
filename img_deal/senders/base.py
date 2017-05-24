# coding: utf8

from settings import config
from app.tasks import send


class SMSSenderBase(object):

    def __init__(self):
        pass

    def send(self, mobile, tpl_id, tpl_value, uid, buyer_nick, sign_name=config.DEFAULT_SMS_SIGN, time=None):
        # TODO: check meizhe balance / black words ?

        # step 1. build data
        data = self.data_maker(tpl_id, tpl_value, mobile, uid, buyer_nick, sign_name)
        if data.get('error'):
            return data['error'], data['black_words']

        # step 2. send msg
        r, _id = self.send_msg(data, time=time)

        return r, _id

    def data_maker(self, tpl_id, tpl_value, mobile, uid, buyer_nick, sign_name):
        pass

    def send_msg(self, data, url=None, time=None):
        pass

    @staticmethod
    def query_task_by_id(task_id):
        r = send.send_msg.AsyncResult(task_id)

        return r.status, r.result
