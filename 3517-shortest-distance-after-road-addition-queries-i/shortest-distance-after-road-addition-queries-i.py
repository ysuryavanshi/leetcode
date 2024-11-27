class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]

        def get_distance():
            q = deque([(0, 0)])
            visited = set()
            visited.add(0)
            while q:
                cur, distance = q.popleft()
                if cur == n - 1:
                    return distance
                else:
                    nxt = cur + 1
                    if nxt not in visited:
                            q.append((nxt, distance + 1))
                            visited.add(nxt)
                    for nxt in graph[cur]:
                        if nxt not in visited:
                            q.append((nxt, distance + 1))
                            visited.add(nxt)

        res = []
        for src, dst in queries:
            graph[src].append(dst)
            res.append(get_distance())
        return res
