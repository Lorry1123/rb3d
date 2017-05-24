# coding: utf8

import requests
from img_deal.actions import image_act

from img_deal.celery_app import celery


@celery.task
def make_3d(name):
    ret = image_act.make_3d_pic(name)
    # TODO: send msg
    return ret


@celery.task
def add(a, b):
    return a + b


def send():
    pass
