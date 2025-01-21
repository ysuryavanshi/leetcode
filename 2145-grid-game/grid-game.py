class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_sum = [[], []]
        n = len(grid[0])

        for i in range(2):
            last = 0
            for j in range(n):
                last += grid[i][j]
                prefix_sum[i].append(last)
        
        res = float('inf')
        for i in range(n):
            sec1 = prefix_sum[0][-1] - prefix_sum[0][i]
            sec2 = prefix_sum[1][i - 1] if i > 0 else 0
            res = min(res, max(sec1, sec2))
        return res