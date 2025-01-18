class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = {
            1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]
        }
        q = deque([(0, 0, 0)])
        min_cost = {(0,0): 0}

        while q:
            row, col, cost = q.popleft()
            if (row, col) == (m - 1, n - 1):
                return cost
            
            for d in directions:
                dr, dc = directions[d]
                nr, nc = row + dr, col + dc
                ncost = cost if d == grid[row][col] else cost + 1

                if nr < 0 or nc < 0 or nr == m or nc == n or ncost >= min_cost.get((nr, nc), float('inf')):
                    continue
                
                min_cost[(nr, nc)] = ncost
                if d == grid[row][col]:
                    q.appendleft((nr, nc, ncost))
                else:
                    q.append((nr, nc, ncost))
