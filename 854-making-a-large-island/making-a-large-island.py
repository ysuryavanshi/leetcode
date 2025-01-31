class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def out_of_bounds(r, c):
            return (r < 0 or c < 0 or r == n or c == n)

        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] != 1:
                return 0
            
            size = 1
            grid[r][c] = label
            neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in neighbors:
                size += dfs(nr, nc, label)
            return size
            
        
        label = 2
        area_dict = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area_dict[label] = dfs(r, c, label)
                    label += 1

        def connect(r, c):
            area = 1
            visited = set([0])
            neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in neighbors:
                if out_of_bounds(nr, nc) or grid[nr][nc] in visited:
                    continue
                visited.add(grid[nr][nc])
                area += area_dict[grid[nr][nc]]
            return area

        res = 0 if not area_dict else max(area_dict.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    res = max(connect(r, c), res)
        
        return res