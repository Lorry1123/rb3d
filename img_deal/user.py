from flask import Flask, Blueprint, render_template, request, jsonify, Response, session, redirect
from img_deal.actions import user as user_act

user = Blueprint('user', __name__, template_folder="templates", static_folder="static")


@user.route('/logout')
def logout():
    if 'uid' in session:
        session.pop('uid')

    return redirect('../img_deal/index')


@user.route('/login_check', methods=['GET', 'POST'])
def login_check():
    uid = request.values.get('uid')
    psw = request.values.get('psw')

    if not uid or not psw:
        return jsonify(status=-1, error='uid or psw is empty')

    # r = 0
    # li = 0
    if 'uid' in session and session['uid'] == uid:
        r = 0
    else:
        r, li = user_act.find_user(dict(uid=uid, psw=psw))

    if not r:
        session['uid'] = uid
        return jsonify(status=0, msg='ok')
    else:
        return jsonify(status=-2, error='uid or psw is wrong')


@user.route('/regist', methods=['GET', 'POST'])
def regist():
    uid = request.values.get('uid')
    psw = request.values.get('psw')
    mobile = request.values.get('mobile')

    if not uid or not psw or not mobile:
        return jsonify(status=-1, error='some fields are empty')

    r = user_act.create_user(dict(uid=uid, psw=psw, mobile=mobile))

    return jsonify(status=r)
