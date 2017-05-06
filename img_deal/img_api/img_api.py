# coding: utf8

from flask import Flask, Blueprint, Response, request, jsonify
import json
import datetime
import requests
import hashlib
from PIL import Image
from img_deal.actions import image_act as img_act

test = Blueprint('test', __name__)
DEFAULT_IMAGE_PATH = 'img_deal/img_api/img/'


@test.route('/get_pic', methods=['POST', 'GET'])
@test.route('/get_pic/<string:name>', methods=['POST', 'GET'])
def get_pic(name=''):
    print name
    img = file(DEFAULT_IMAGE_PATH + name + '.jpg')
    resp = Response(img, mimetype="image/jpeg")

    return resp


@test.route('/get_3d_pic/<string:name>', methods=['POST', 'GET'])
def get_3d_pic(name=''):
    ret = img_act.make_3d_pic(name)
    resp = Response(ret, mimetype='image/jpeg')

    return resp


@test.route('/upload_pic', methods=['POST', 'GET'])
@test.route('/upload_pic/<string:name>', methods=['POST', 'GET'])
def upload_pic(name=''):
    # name = request.values.get('name')
    print 'name:', name
    file_tmp = request.files['file']
    img = Image.open(file_tmp)
    # img.save(DEFAULT_IMAGE_PATH + name + '.jpg', 'jpeg')
    # img_act.save_to_db(name)

    return jsonify(status=0, src='../img_api/get_pic/' + name)


# @test.route('/send_msg_yunpian', methods=['POST', 'GET'])
# def send_msg_yunpian():
#     phone = request.values.get('phone')
#     name = request.values.get('name')
#     obj = request.values.get('obj')
#     detail = request.values.get('detail')
#
#     print phone, name, obj, detail
#
#     url = 'https://sms.yunpian.com/v2/sms/single_send.json'
#
#     text = '【路哦汝衣网】用户sama～您在{}定制的{}已经制作完成了哦～～请登陆{}查看呢～\n以下为订单信息：{}'.format(name, obj, name, detail)
#     print text
#     data = {
#         'apikey': '44fb01a4a9f4aea703876e18606cbc5b',
#         'mobile': phone,
#         'text': text
#     }
#     resp = requests.post(url, data)
#     print 'success'
#     resp.encoding = 'utf-8'
#     ret = resp.text
#     print resp.text
#     print data
#
#     return Response(json.dumps({'msg': ret}), mimetype='application/json')
#
#
# @test.route('/send_msg_alidayu', methods=['POST', 'GET'])
# def send_msg_alidayu():
#     phone = request.values.get('phone')
#     name = request.values.get('name')
#     obj = request.values.get('obj')
#     detail = request.values.get('detail')
#     app_secret = '65c7688b51a06aa1b307d12391000f0b'
#
#     print 'json ---->', json.dumps(dict(name=name, object=obj, detail=detail))
#
#     data = dict(
#         # single send params
#         sms_param=json.dumps(dict(name=name, object=obj, detail=detail)),
#         sms_type='normal',
#         sms_free_sign_name='南理校内帮',
#         rec_num=phone,
#         sms_template_code='SMS_59100027',
#
#         # common params
#         method='alibaba.aliqin.fc.sms.num.send',
#         app_key='23725539',
#         sign_method='md5',
#         # TODO: get sign
#         timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         format='json',
#         v='2.0'
#     )
#
#     sign = get_sign(app_secret, data)
#     print 'sign:  %s' % sign
#
#     url = 'http://gw.api.taobao.com/router/rest'
#
#     data['sign'] = sign
#     resp = requests.post(url, data)
#     print 'success'
#     resp.encoding = 'utf-8'
#     ret = resp.text
#     print resp.text
#
#     return Response(json.dumps({'msg': ret}), mimetype='application/json')
#
#
# def get_sign(secret, params):
#     keys = params.keys()
#     keys.sort()
#
#     for key in keys:
#         print key
#
#     params = "%s%s%s" % (secret,
#                          str().join('%s%s' % (key, params[key]) for key in keys),
#                          secret)
#     print params
#     sign = hashlib.md5(params).hexdigest().upper()
#
#     return sign
