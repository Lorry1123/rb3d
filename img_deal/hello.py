from flask import Flask, Blueprint, render_template, request, jsonify, Response, session
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


