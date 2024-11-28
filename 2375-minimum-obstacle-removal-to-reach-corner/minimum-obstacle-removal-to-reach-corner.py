class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        min_heap = [(0,0,0)]
        heapify(min_heap)
        visited[0][0] = 1
        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if x == m - 1 and y == n - 1:
                return cost
            if x > 0 and not visited[x-1][y]:
                visited[x-1][y] = 1
                heapq.heappush(min_heap, (cost + grid[x-1][y], x-1, y))
            if y < n - 1 and not visited[x][y+1]:
                visited[x][y+1] = 1
                heapq.heappush(min_heap, (cost + grid[x][y+1], x, y+1))
            if x < m - 1 and not visited[x+1][y]:
                visited[x+1][y] = 1
                heapq.heappush(min_heap, (cost + grid[x+1][y], x+1, y))
            if y > 0 and not visited[x][y-1]:
                visited[x][y-1] = 1
                heapq.heappush(min_heap, (cost + grid[x][y-1], x, y-1))