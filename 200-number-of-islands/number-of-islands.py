class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '0' or visited[row][col]:
                    continue
                
                visited[row][col] = True
                res += 1
                stack = deque([(row, col)])
                while stack:
                    x, y = stack.popleft()
                    neighbors = [(x+1,y), (x-1,y), (x,y+1), (x, y-1)]
                    for nr, nc in neighbors:
                        if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and not visited[nr][nc]):
                            visited[nr][nc] = True
                            stack.append((nr, nc))
        return res