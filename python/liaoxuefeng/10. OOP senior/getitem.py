class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start, stop = n.start, n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            res = []
            for x in range(stop):
                if x >= start:
                    res.append(a)
                a, b = b, a + b
            return res


if __name__ == "__main__":
    fib = Fib()
    print(fib[:10:2])