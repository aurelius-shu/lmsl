from functools import reduce

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': '.'
}


def char2num(c):
    return DIGITS[c]


def str2float(s):
    def str2int(s):
        return reduce(lambda x1, x2: x1 * 10 + x2,
                      map(char2num, [c for c in s if c != '.']))

    return str2int(s) / (10**s[::-1].index('.'))


def str2float2(s):
    point = 0

    def to_float(i, c):
        nonlocal point
        if not isinstance(c, int):
            point = 1
            return i
        if point == 0:
            return i * 10 + c
        else:
            point *= 10
            return i + c / point

    return reduce(to_float, map(char2num, s))


if __name__ == "__main__":
    print(str2float('123.456'))
    print(str2float2('123.456'))