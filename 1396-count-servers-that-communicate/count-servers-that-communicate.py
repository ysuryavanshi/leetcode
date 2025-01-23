class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        servers = set()
        for i in range(ROWS):
            connected = []
            for j in range(COLS):
                if grid[i][j]:
                    connected.append((i,j))

            if len(connected) > 1:
                servers.update(connected)

        for j in range(COLS):
            connected = []
            for i in range(ROWS):
                if grid[i][j]:
                    connected.append((i,j))

            if len(connected) > 1:
                servers.update(connected)

        return len(servers)