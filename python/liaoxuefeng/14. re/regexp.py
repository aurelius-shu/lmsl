import re


def name_of_email(addr):
    m = re.match(r'^([a-zA-Z\d\s\<\>]+)\@(voyager|example)\.(org|com)$', addr)
    if not m:
        return None
    m = re.match(r'^\<([a-zA-Z\s]+)\>[\s]+[a-zA-Z\d]+|([a-zA-Z\d]+)$',
                 m.group(1))

    return m.group(1) if m and m.group(1) else m.group(2)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')