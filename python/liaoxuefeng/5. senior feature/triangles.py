def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


def test_next():
    triangle = triangles()
    for i in range(10):
        print(next(triangle))


def test_for():
    n = 10
    triangle = triangles()
    for t in triangle:
        print(t)
        n -= 1
        if n < 1:
            break


if __name__ == "__main__":
    test_next()
    test_for()
