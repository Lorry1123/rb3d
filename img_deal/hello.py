from flask import Flask, Blueprint, render_template, request, jsonify, Response, session
from img_deal.img_api import ImageReader
from img_deal.actions import user
from img_deal.ext.decorators import login_required

IMG_DEAL_NAME = 'img_deal'

img_deal = Blueprint('img_deal', __name__, template_folder="templates", static_folder="static")


DEFAULT_IMAGE_PATH = 'img_deal/img_api/img/'


@img_deal.route('/index')
def index():
    return render_template('index.html')


@img_deal.route('/login')
def login():
    return render_template('login_v2.html')


@img_deal.route('/list', methods=['GET', 'POST'])
@login_required
def list_page():
    return render_template('list.html')


@img_deal.route('/fast_make', methods=['GET', 'POST'])
@login_required
def fast_make():
    return render_template('fastPage.html')


@img_deal.route('/test')
def test():
    return render_template('testPage.html')


@img_deal.route('/img')
def image():
    img = ImageReader(path=DEFAULT_IMAGE_PATH, name='img_upload')
    img.calc_lov(size=3)
    img.show_lov(show=False)
    img.calc_deep_map()
    img.red_blue_translation()

    ret = file(DEFAULT_IMAGE_PATH + 'img_upload_3d' + '.jpg')
    resp = Response(ret, mimetype='image/jpeg')

    return resp


# @img_deal.route('/login')
# def login():
#     return render_template('login_v2.html')
#
#
# @img_deal.route('/login_check', methods=['GET', 'POST'])
# def login_check():
#     uid = request.values.get('uid')
#     psw = request.values.get('psw')
#
#     if not uid or not psw:
#         return jsonify(status=-1, error='uid or psw is empty')
#
#     # r = 0
#     # li = 0
#     if 'uid' in session and session['uid'] == uid:
#         r = 0
#     else:
#         r, li = user.find_user(dict(uid=uid, psw=psw))
#
#     if not r:
#         session['uid'] = uid
#         return jsonify(status=0, msg='ok')
#     else:
#         return jsonify(status=-2, error='uid or psw is wrong')
#
#
# @img_deal.route('/regist', methods=['GET', 'POST'])
# def regist():
#     uid = request.values.get('uid')
#     psw = request.values.get('psw')
#     mobile = request.values.get('mobile')
#
#     if not uid or not psw or not mobile:
#         return jsonify(status=-1, error='some fields are empty')
#
#     r = user.create_user(dict(uid=uid, psw=psw, mobile=mobile))
#
#     return jsonify(status=r)


