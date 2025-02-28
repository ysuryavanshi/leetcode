class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        @cache
        def helper(i, j):
            if (i, j) == (ROWS - 1, COLS - 1):
                return grid[i][j]
            if i == ROWS or j == COLS:
                return float('inf')
            
            return grid[i][j] + min(helper(i + 1, j), helper(i, j + 1))

        return helper(0, 0)