from hashlib import md5

def md5Encode(data):
    value = ""

    if type(data) == dict or type(data) == list:
        for i in data:
            value += data[i]
    else:
        value += data

    return md5(value.encode('utf-8')).hexdigest()
