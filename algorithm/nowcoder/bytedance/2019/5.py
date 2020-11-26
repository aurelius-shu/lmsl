n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

V = 1 << (n - 1)
dp = [[float('inf')] * V for i in range(n)]
for i in range(n):
    dp[i][0] = matrix[i][0]

for j in range(1, V):
    for i in range(n):
        if (i < 1 and ((j << (1 - i)) & 1) == 0) or ((i >= 1 and (j >> (i - 1)) & 1) == 0):
            for k in range(1, n):
                if ((j >> (k - 1)) & 1) == 1:
                    dp[i][j] = min(dp[i][j], matrix[i][k] + dp[k][j ^ (1 << (k - 1))])
print(dp[0][V - 1])
