class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        computers = []
        rows_count, cols_count = [0] * ROWS, [0] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    computers.append((i, j))
                    rows_count[i] += 1
                    cols_count[j] += 1
        
        res = 0
        for i, j in computers:
            if rows_count[i] > 1 or cols_count[j] > 1:
                res += 1
        return res