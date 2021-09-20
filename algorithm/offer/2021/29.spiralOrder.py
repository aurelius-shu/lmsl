class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        row_counts, col_counts = len(matrix), len(matrix[0])
        layer = 0
        result = []

        while layer * 2 < min(row_counts, col_counts):
            # (layer, layer -> col_counts-layer-1)
            result += [matrix[layer][i] for i in range(layer, col_counts - layer)]
            # (layer+1 -> row_counts-layer-1, col_counts-layer-1)
            result += [matrix[i][col_counts - layer - 1] for i in range(layer + 1, row_counts - layer)]
            # (row_counts-layer-1, col_counts-layer-2 -> layer)
            if layer * 2 + 1 < row_counts:
                result += [matrix[row_counts - layer - 1][i] for i in range(col_counts - layer - 2, layer - 1, -1)]
            # (row_counts-layer-2 -> layer+1, layer)
            if layer * 2 + 1 < col_counts:
                result += [matrix[i][layer] for i in range(row_counts - layer - 2, layer, -1)]
            layer += 1
        return result


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = s.spiralOrder(matrix)
    print(result)
