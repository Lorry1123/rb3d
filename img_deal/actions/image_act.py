# coding: utf8

from img_deal.img_api.ImageReader import ImageReader
from img_deal.actions import img as img_db
from flask import session

DEFAULT_IMAGE_PATH = 'img_deal/img_api/img/'


def make_3d_pic(name):
    img = ImageReader(path=DEFAULT_IMAGE_PATH, name=name)
    img.calc_lov(size=3)
    img.show_lov(show=False)
    img.calc_deep_map()
    img.red_blue_translation()

    ret = file(DEFAULT_IMAGE_PATH + name + '_3d' + '.jpg')
    return ret


def save_to_db(name):
    img = dict(uid=session['uid'], name=name)
    r, exist_img = img_db.find_img(img)
    if r:
        print 'save img'
        img_db.create_img(img)


def make_lov(name, area, threshold, size):
    img = ImageReader(path=DEFAULT_IMAGE_PATH, name=name)
    img.calc_lov(size=size, area=area, threshold=threshold)
    img.show_lov(show=False)

    ret = file(DEFAULT_IMAGE_PATH + name + '_lov.jpg')

    return ret


def make_3d_pic_enhanced(name, area, threshold, size, screen, send_to_task=0):
    img = ImageReader(path=DEFAULT_IMAGE_PATH, name=name)
    img.calc_lov(size=size, area=area, threshold=threshold)
    img.show_lov(show=False)

    img.set_screen(screen['width'], screen['height'], screen['size'])

    img.calc_deep_map()
    img.red_blue_translation()

    if not send_to_task:
        ret = file(DEFAULT_IMAGE_PATH + name + '_3d' + '.jpg')
        return ret
