def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    oi = _odd_iter()
    while True:
        n = next(oi)
        yield n
        oi = filter(_not_divisible(n), oi)


if __name__ == "__main__":
    for n in primes():
        if n < 100:
            print(n)
        else:
            break