# coding: utf8

from img_deal.ext.mongoket import Collection
from . import db


@db.register
class Img(Collection):
    __collection__ = 'img'
    structure = {
        'uid': basestring,
        'name': basestring,
    }
    required_fields = ['uid', 'name'],
    default_values = {
    }
    indexes = [
        {'fields': 'uid', 'unique': True},
    ]
