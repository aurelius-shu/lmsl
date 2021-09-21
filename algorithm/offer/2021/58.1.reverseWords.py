class Solution:
    def reverseWords(self, s):
        splits = s.split(' ')
        splits = [s[::-1] for s in splits if s]
        return ' '.join(splits)[::-1]
