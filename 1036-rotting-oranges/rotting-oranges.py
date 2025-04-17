class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = [[0] * COLS for _ in range(ROWS)]
        res = fresh_oranges = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = 1

                if grid[i][j] == 1:
                    fresh_oranges += 1

        if not fresh_oranges:
            return 0
        if not q:
            return -1
        
        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for dx, dy in neighbors:
                    if dx < 0 or dy < 0 or dx == ROWS or dy == COLS or visited[dx][dy] or grid[dx][dy] != 1:
                        continue
                    
                    fresh_oranges -= 1
                    visited[dx][dy] = 1
                    q.append((dx, dy))

        return res - 1 if not fresh_oranges else -1