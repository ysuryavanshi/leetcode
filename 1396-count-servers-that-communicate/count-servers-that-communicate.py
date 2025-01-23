class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers = set()
        for i in range(len(grid)):
            connected = []
            for j in range(len(grid[0])):
                if grid[i][j]:
                    connected.append((i,j))

            if len(connected) > 1:
                servers.update(connected)

        for j in range(len(grid[0])):
            connected = []
            for i in range(len(grid)):
                if grid[i][j]:
                    connected.append((i,j))

            if len(connected) > 1:
                servers.update(connected)

        return len(servers)