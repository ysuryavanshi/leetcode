class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))
            while q:
                cur, distance = q.popleft()
                if cur == n-1:
                    return distance
                for neigh in adj[cur]:
                    if neigh not in visit:
                        q.append((neigh, distance + 1))
                        visit.add(neigh)

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res