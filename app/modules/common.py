import hashlib


def md5(sign):
    m = hashlib.md5(sign)
    return m.hexdigest()
