from flask import make_response
from functools import wraps
from json import dumps

def jsonResponse(callback):
    @wraps(callback)
    def decorated(*args, **kwargs):
        JSON = dumps(dict(callback(*args, **kwargs)), indent=4, sort_keys=True)
        response = make_response(JSON)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        response.headers['mimetype'] = 'application/json'
        response.status_code = 200
        return response
    return decorated