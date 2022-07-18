result = set()


def algo(chars, index):
    if not chars:
        raise Exception('chars is none type.')
    if index == len(chars) - 1:
        global result
        result.add(''.join(chars))
        return
    for i in range(len(chars)):
        chars[i], chars[index] = chars[index], chars[i]
        algo(chars, index+1)
        chars[i], chars[index] = chars[index], chars[i]


chars = ['a', 'b', 'c', 'd', 'e']
algo(chars, 0)
print(result)
print(len(result))
