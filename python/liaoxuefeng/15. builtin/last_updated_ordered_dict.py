from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):

        containKey = 1 if key in self else 0
        print(len(self))
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


if __name__ == "__main__":
    ld = LastUpdatedOrderedDict(capacity=4)
    ld['a'] = 1
    ld['b'] = 2
    ld['c'] = 3
    ld['d'] = 4
    print(ld)
    ld['e'] = 5
    print(ld)
    ld['e'] = 55
    print(ld)