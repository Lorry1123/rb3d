# coding: utf8

from img_deal.ext.mongoket import Collection
from . import db


@db.register
class User(Collection):
    __collection__ = 'user'
    structure = {
        'uid': basestring,
        'psw': basestring
    }
    required_fields = ['uid', 'nick', 'psw'],
    default_values = {
    }
    indexes = [
        {'fields': 'uid', 'unique': True},
        {'fields': 'nick', 'unique': True}
    ]