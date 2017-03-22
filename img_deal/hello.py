from flask import Flask,Blueprint,render_template

IMG_DEAL_NAME = 'img_deal'

img_deal = Blueprint('img_deal', __name__, template_folder="templates", static_folder="static")


@img_deal.route('/hello')
def hello():
    return 'hello from img_deal'


@img_deal.route('/index')
def index():
    return render_template('layout.html')


@img_deal.route('/test')
def test():
    return render_template('testPage.html')
