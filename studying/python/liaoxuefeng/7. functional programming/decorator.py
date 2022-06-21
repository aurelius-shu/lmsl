import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}():')
        return func(*args, **kwargs)

    return wrapper


def log(info):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{info} {func.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return decorator