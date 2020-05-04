from functools import wraps


def count(f):
    @wraps(f)
    def inner(*args, **kwargs):
        inner.counter += 1
        return f(*args, **kwargs)
    inner.counter = 0
    return inner
