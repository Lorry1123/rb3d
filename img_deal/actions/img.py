# coding: utf8

from img_deal.models import db


def create_img(img):
    # test
    con = db.Img()
    con.update(img)

    con.save()
    return 0


def find_img(img):
    r = list(db.Img.collection.find(img))

    if r:
        return 0, r
    else:
        return -1, r
