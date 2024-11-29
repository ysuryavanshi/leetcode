class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        min_heap = [(0,0,0)] # cost, x, y
        heapify(min_heap)
        visited = set()

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if x == m - 1 and y == n - 1:
                return cost

            if x + 1 < m and (x + 1, y) not in visited:
                c = max(cost + 1, grid[x+1][y] + (grid[x+1][y] - cost + 1) % 2)
                heapq.heappush(min_heap, (c, x + 1, y))
                visited.add((x + 1, y))

            if y + 1 < n and (x, y + 1) not in visited:
                c = max(cost + 1, grid[x][y+1] + (grid[x][y+1] - cost + 1) % 2)
                heapq.heappush(min_heap, (c, x, y+1))
                visited.add((x, y + 1))

            if x - 1 >= 0 and (x - 1, y) not in visited:
                c = max(cost + 1, grid[x-1][y] + (grid[x-1][y] - cost + 1) % 2)
                heapq.heappush(min_heap, (c, x - 1, y))
                visited.add((x - 1, y))

            if y - 1 >= 0 and (x, y - 1) not in visited:
                c = max(cost + 1, grid[x][y-1] + (grid[x][y-1] - cost + 1) % 2)
                heapq.heappush(min_heap, (c, x, y-1))
                visited.add((x, y - 1))
