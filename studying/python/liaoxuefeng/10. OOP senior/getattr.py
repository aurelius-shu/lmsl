class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __call__(self, param):
        return Chain(f'{self._path}/{param}')

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == "__main__":
    print(Chain().status.user('Aurelius').timeline.list)