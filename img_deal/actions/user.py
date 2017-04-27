# coding: utf8

from img_deal.models import db


def create_user(user):
    # test
    con = db.User()
    con.update(user)

    con.save()
    return 0


def find_user(user):
    r = list(db.User.collection.find(user))

    if r:
        return 0, r
    else:
        return -1, r
