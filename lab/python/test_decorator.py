import functools



def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('call %sds' % func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2018-11-01')


now()