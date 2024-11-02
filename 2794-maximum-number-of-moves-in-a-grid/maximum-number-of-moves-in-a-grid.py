class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        ans = 0
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            moves = 0
            for r, c in [(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
                if 0 <= r < m and 0 <= c < n and grid[r][c] > grid[i][j]:
                    moves = max(moves, 1 + dfs(r, c))
            dp[i][j] = moves
            return moves

        for i in range(m):
            ans = max(ans, dfs(i, 0))
        
        return ans