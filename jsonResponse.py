from flask import make_response
from functools import wraps
from json import dumps

def jsonResponse(callback):
    @wraps(callback)
    def decorated(*args, **kwargs):
        function = callback(*args, **kwargs)
        JSON = dumps(function, indent=4, sort_keys=True)
        response = make_response(JSON)
        response.headers['content-type'] = 'application/json; charset=utf-8'
        return response
    return decorated