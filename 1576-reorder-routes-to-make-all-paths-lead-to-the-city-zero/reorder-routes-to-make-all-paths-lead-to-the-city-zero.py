class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append((y, True))
            graph[y].append((x, False))

        count = 0
        q = deque([0])
        visited = set()

        while q:
            city = q.popleft()
            visited.add(city)
            for nd, st in graph[city]:
                if nd not in visited:
                    q.append(nd)
                    if st: count += 1
        return count