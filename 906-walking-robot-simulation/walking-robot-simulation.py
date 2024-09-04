class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        x, y, d = (0,0,0)
        directions = [(0, 1), (1,0), (0,-1), (-1,0)]
        max_d = 0
        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = x + directions[d][0], y + directions[d][1]
                    if (dx, dy) in obstacles:
                        break
                    x, y = dx, dy
                    max_d = max(max_d, x * x + y * y)
        return max_d
