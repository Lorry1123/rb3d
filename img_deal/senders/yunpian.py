# coding: utf8

import requests
from datetime import datetime

from settings import SenderYunpianConfig
from .base import SMSSenderBase
from app.tasks.send import add_sign, add_template, send_msg


class YunPianSender(SMSSenderBase, SenderYunpianConfig):
    def __init__(self, batch_sender=False, yingxiao=False):
        super(YunPianSender, self).__init__()

        self.post_url = self.SINGLE_SEND_API_URL

        if batch_sender:
            self.post_url = self.MULTI_SEND_API_URL

        if yingxiao:
            self.default_common_params = {
                'apikey': self.YINGXIAO_KEY,
            }
        else:
            self.default_common_params = {
                'apikey': self.APP_KEY,
            }

    def data_maker(self, tpl_id, tpl_value, mobile, uid, buyer_nick, sign_name):
        # step 1. fill default common params
        params = dict.copy(self.default_common_params)

        # step 2. fill send params
        params.update(self.fill_send_params(tpl_id, tpl_value, mobile))

        # step 3. check black words
        r = requests.post(self.BLACK_WORDS_API, params)
        # print r.text
        if len(eval(r.text)):
            return dict(error='black words!!', black_words=r.text)

        # 额外参数需要在 pull status 回传的打包放uid里,暂时是单发，不做群发的处理
        params.update({'uid': uid})
        params.update({'buyer_nick': buyer_nick})

        return params

    def fill_send_params(self, tpl_id, tpl_value, mobile):
        tpl_value = eval(tpl_value)
        if not isinstance(tpl_value, list):
            tpl_value = [tpl_value]

        r = self.query_template(tpl_id)
        tpl_content = eval(r.replace('null', 'None'))['tpl_content']
        flag = 1
        if tpl_content[0] == '#':
            flag = 0
        tpl_content = tpl_content.split('#')
        text = []
        for i in range(len(mobile.split(','))):
            value = tpl_value[i]
            tmp = ''
            for j in range(len(tpl_content)):
                if j % 2 == flag:
                    tmp += value[tpl_content[j]]
                else:
                    tmp += tpl_content[j]
            text.append(tmp)

        text = ','.join(text)

        ret = dict(text=text, mobile=mobile)
        return ret

    def send_msg(self, data, url=None, time=None):
        if not url:
            url = self.post_url

        # _id = send_msg.delay(data, url).id
        if time:
            _id = send_msg.apply_async(args=[data, url], eta=time)
        else:
            _id = send_msg.delay(data, url)
        return 1, str(_id)

    def set_single_or_batch(self, s):
        # 暂时没有用到，目前没觉得有什么需要使用batch send的场景，即使有，也可以用multi send
        if s == 'batch':
            self.post_url = self.BATCH_SEND_API_URL
        elif s == 'single':
            self.post_url = self.SINGLE_SEND_API_URL
        elif s == 'multi':
            self.post_url = self.MULTI_SEND_API_URL
        else:
            return '暂不支持'

        return 'success'

    def query_by_mobile(self, num):
        params = dict.copy(self.default_common_params)
        time = dict(start_time='2017-01-01 00:00:00', end_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        params.update(time)
        if num:
            params.update({'mobile': num})

        r = requests.post(self.QUERY_BY_MOBILE_API_URL, params)

        return r.text

    def add_sign(self, sign, notify=False):
        params = dict.copy(self.default_common_params)
        params.update({'sign': sign, 'notify': notify})
        url = self.ADD_SIGN_API

        r = add_sign.delay(params, url)

        return 'add sign post', r.id

    def query_sign(self, sign):
        params = dict.copy(self.default_common_params)
        if sign:
            params.update({'sign': sign})
        url = self.QUERY_SIGN_API

        r = requests.post(url, params)

        return r.text

    def add_template(self, text, notify=3):
        params = dict.copy(self.default_common_params)
        params.update({'tpl_content': text, 'notify_type': notify})
        url = self.ADD_TEMPLATE_API

        r = add_template.delay(params, url)

        return r.get()

    def query_template(self, tpl_id=None):
        params = dict.copy(self.default_common_params)

        if tpl_id:
            params.update({'tpl_id': tpl_id})
        url = self.QUERY_TEMPLATE_API

        r = requests.post(url, params)

        return r.text

    def add_yingxiao_sign(self, sign, notify=False):
        params = dict(apikey=self.YINGXIAO_KEY, sign=sign, notify=notify)
        url = self.ADD_SIGN_API

        r = add_sign.delay(params, url)

        return 'add sign post', r.id

