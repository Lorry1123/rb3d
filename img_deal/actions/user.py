# coding: utf8

from img_deal.models import db


def create_user(user):
    # test
    con = db.User()
    con.update(user)

    con.save()
    return 0
