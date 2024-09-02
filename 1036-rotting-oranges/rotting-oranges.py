class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: return -1

        n = len(grid[0])
        fresh_count = 0
        rotten = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0
        while rotten and fresh_count > 0:
            minutes += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == m or yy < 0 or yy == n: continue
                    if grid[xx][yy] in [0, 2]: continue

                    fresh_count -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        
        return minutes if fresh_count == 0 else -1