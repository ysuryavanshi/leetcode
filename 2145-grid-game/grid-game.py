class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float('inf')
        sum_r1 = sum(grid[0])
        sum_r2 = 0

        for i in range(len(grid[0])):
            sum_r1 -= grid[0][i]
            res = min(res, max(sum_r1, sum_r2))
            sum_r2 += grid[1][i]
        return res