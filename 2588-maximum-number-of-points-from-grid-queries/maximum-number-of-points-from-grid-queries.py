class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        heapify(min_heap)
        ans = {}
        cur_ans = 0

        for query in sorted(queries):
            while min_heap and query > min_heap[0][0]:
                _, x, y = heappop(min_heap)
                neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                cur_ans += 1

                for dx, dy in neighbors:
                    if dx < 0 or dy < 0 or dx == ROWS or dy == COLS or visited[dx][dy]:
                        continue

                    visited[dx][dy] = True
                    heappush(min_heap, (grid[dx][dy], dx, dy))
            ans[query] = cur_ans
        
        return [ans[query] for query in queries]