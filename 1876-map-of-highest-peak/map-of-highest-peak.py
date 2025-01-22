class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque([])
        visited = set()        
        res = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i,j))
                    visited.add((i,j))
                    res[i][j] = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            r, c = q.popleft()
            val = res[r][c] + 1

            for dx, dy in directions:
                nr, nc = r + dx, c + dy

                if nr < 0 or nc < 0 or nr == m or nc == n or (nr, nc) in visited:
                    continue
                
                q.append((nr, nc))
                visited.add((nr, nc))
                res[nr][nc] = val
        
        return res