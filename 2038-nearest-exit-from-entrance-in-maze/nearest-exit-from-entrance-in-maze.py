class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(*entrance, 0)])
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, c = q.popleft()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and [x, y] != entrance:
                return c
            for i, j in [(x + p, y + q) for p, q in directions]:
                if 0 <= i < m and 0 <=j < n and maze[i][j] == '.':
                    maze[i][j] = '+'
                    q.append((i, j, c + 1))
        return -1
