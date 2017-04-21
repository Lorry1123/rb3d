from flask import Flask, Blueprint, render_template
from img_deal.img_api import ImageReader

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
    img = ImageReader(path=DEFAULT_IMAGE_PATH)
    # img.decode(DEFAULT_IMAGE_PATH)
    img.calc_lov(size=3)
    img.show_lov()
    return 'success'
