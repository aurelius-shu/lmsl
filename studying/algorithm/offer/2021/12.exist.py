class Solution:
    def __init__(self):
        self.row_counts = 0
        self.col_counts = 0
        self._board = None
        self._m = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        self._board = board
        self.row_counts, self.col_counts = len(board), len(board[0])

        for i in range(self.row_counts):
            for j in range(self.col_counts):
                self._m = [[1 for i in range(self.col_counts)] for j in range(self.row_counts)]
                if self.find(i, j, word):
                    return True
        return False

    def find(self, i, j, word):
        if not word:
            return True
        if i < 0 or i >= self.row_counts or j < 0 or j >= self.col_counts or self._m[i][j] == 0:
            return False
        if self._board[i][j] == word[0]:
            self._m[i][j] = 0
            if self.find(i - 1, j, word[1:]) or \
                    self.find(i + 1, j, word[1:]) or \
                    self.find(i, j - 1, word[1:]) or \
                    self.find(i, j + 1, word[1:]):
                return True
            else:
                self._m[i][j] = 0
                return False
