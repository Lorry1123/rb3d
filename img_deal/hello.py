from flask import Flask, Blueprint, render_template, request, jsonify
from img_deal.img_api import ImageReader
from img_deal.actions import user


IMG_DEAL_NAME = 'img_deal'

img_deal = Blueprint('img_deal', __name__, template_folder="templates", static_folder="static")


DEFAULT_IMAGE_PATH = 'img_deal/img_api/img/'


@img_deal.route('/hello')
def hello():
    return 'hello from img_deal'


@img_deal.route('/index')
def index():
    return render_template('layout.html')


@img_deal.route('/test')
def test():
    return render_template('testPage.html')


@img_deal.route('/img')
def image():
    img = ImageReader(path=DEFAULT_IMAGE_PATH, name='lena')
    # img.calc_lov(size=3)
    # img.show_lov(DEFAULT_IMAGE_PATH, name='zebra')
    img.calc_deep_map(debug_mode=True)
    img.red_blue_translation()
    return 'success'


@img_deal.route('/login')
def login():
    return render_template('login.html')


@img_deal.route('/login_check', methods=['GET', 'POST'])
def login_check():
    uid = request.values.get('uid')
    psw = request.values.get('psw')

    if not uid or not psw:
        return jsonify(status=-1, error='uid or psw is empty')

    r, li = user.find_user(dict(uid=uid, psw=psw))

    print r, li

    if not r:
        return jsonify(status=0, msg='ok')
    else:
        return jsonify(status=-2, error='uid or psw is wrong')


@img_deal.route('/regist', methods=['GET', 'POST'])
def regist():
    uid = request.values.get('uid')
    psw = request.values.get('psw')
    mobile = request.values.get('mobile')

    if not uid or not psw or not mobile:
        return jsonify(status=-1, error='some fields are empty')

    r = user.create_user(dict(uid=uid, psw=psw, mobile=mobile))

    return jsonify(status=r)
