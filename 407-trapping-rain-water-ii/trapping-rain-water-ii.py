class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        min_heap = []
        for r in range(m):
            for c in range(n):
                if r in [0, m - 1] or c in [0, n - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        
        res = 0
        max_height = -1

        while min_heap:
            h, r, c = heappop(min_heap)
            max_height = max(h, max_height)
            res += max_height - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if nr < 0 or nr == m or nc < 0 or nc == n or heightMap[nr][nc] == -1:
                    continue
                
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res
