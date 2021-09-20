from functools import reduce


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower().strip()
        if len(s) < 1:
            return False
        if 'e' in s and len(s.split('e')) == 2:
            left, right = s.split('e')
            left, right = left[1:] if left and left[0] in ['+', '-'] else left, \
                          right[1:] if right and right[0] in ['+', '-'] else right
            if len(left) == 0 or len(right) == 0:
                return False
            return self.isFloat(left) and self.isUnSignedInteger(right)
        elif 'e' not in s:
            return self.isFloat(s)
        else:
            return False

    def isFloat(self, s):
        if not reduce(lambda x, y: x and y,
                      [n in ['+', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] for n in str(s)]):
            return False

        if s[0] in ['+', '-']:
            s = s[1:]

        if len(s) < 1:
            return False

        if '.' in s and len(s.split('.')) == 2:
            left, right = s.split('.')
            if len(left) == 0 and len(right) == 0:
                return False
            if (len(left) == 0 or self.isUnSignedInteger(left)) and \
                    (len(right) == 0 or self.isUnSignedInteger(right)):
                return True
            else:
                return False
        elif '.' not in s:
            return self.isUnSignedInteger(s)
        else:
            return False

    def isUnSignedInteger(self, s):
        if not reduce(lambda x, y: x and y,
                      [n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] for n in str(s)]):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isNumber("-1E-16"))
