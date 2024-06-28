from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[0] * n for _ in range(m)]
    ans = 0
    def dfs(i, j):
        # TODO реализовать поиск в глубину
        if i<0 or j<0 or i>m-1 or j>n-1:
            return 0
        else:
            if
            dp[i][j]=sum([dfs(i+di[k][0],j+di[k][1]) for k in range(len(di))])

    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))


longest_increasing_path( [[9,9,4],[6,6,8],[2,1,1]])