class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        n = len(grid)
        
        rows = Counter([tuple(g) for g in grid])

        for i in range(n):
            count += rows.get(tuple(grid[j][i] for j in range(n)), 0)
        return count