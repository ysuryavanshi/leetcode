class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = [[0] * n for _ in range(m)]

        for x, y in walls + guards:
            ans[x][y] = 2

        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx, gy
                while 0 <= x + dx < m and 0 <= y + dy < n and ans[x + dx][y + dy] != 2:
                    x += dx
                    y += dy
                    ans[x][y] = 1

        return sum(row.count(0) for row in ans)