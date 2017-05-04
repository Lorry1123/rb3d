# coding: utf8

import functools

from flask import abort, session


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'uid' in session and session['uid']:
            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper
