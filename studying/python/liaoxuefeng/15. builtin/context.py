class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('query info about %s...' % self.name)


from contextlib import contextmanager


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query2(name)
    yield q
    print('end')


with create_query('bob') as q:
    q.query()