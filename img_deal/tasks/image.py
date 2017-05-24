# coding: utf8

import requests
from img_deal.actions import image_act, sms_sender
from img_deal.celery_app import celery


@celery.task
def make_3d(name, area, threshold, size, screen, session):
    ret = image_act.make_3d_pic_enhanced(name, area, threshold, size, screen, 1)
    # ret = image_act.make_3d_pic(name)
    # TODO: send msg

    print 'send msg'
    print session
    mobile = session['mobile']
    user = session['uid']
    text = '【红蓝3d合成器】尊敬的{}您好，您在「在线红蓝3d图像合成器」中制作的图像已经完成了～请登陆网站在列表页查看哦～'.format(user)

    sms_sender.send(mobile, text)
    return ret


@celery.task
def add(a, b):
    return a + b

