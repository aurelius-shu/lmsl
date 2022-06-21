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
    '9': 9
}


def char2num(c):
    return DIGITS[c]


def str2int(s):
    return reduce(lambda x1, x2: x1 * 10 + x2, map(char2num, s))


if __name__ == "__main__":
    print(str2int('1234'))
