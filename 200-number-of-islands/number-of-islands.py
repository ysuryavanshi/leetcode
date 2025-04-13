class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = [[0] * COLS for _ in range(ROWS)]
        res = 0

        def dfs(i, j):
            q = deque([(i, j)])

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()

                    for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if dx < 0 or dx == ROWS or dy < 0 or dy == COLS or visited[dx][dy] or grid[dx][dy] == '0':
                            continue
                        
                        visited[dx][dy] = True
                        q.append((dx, dy))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                    dfs(i, j)

        return res