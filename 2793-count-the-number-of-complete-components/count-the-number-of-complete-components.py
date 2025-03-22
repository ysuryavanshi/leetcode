class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v, connected):
            if v in visit:
                return
            
            visit.add(v)
            connected.append(v)
            for nei in adj[v]:
                dfs(nei, connected)
            return connected
        
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        res = 0
        visit = set()
        for v in range(n):
            if v in visit:
                continue
            
            components = dfs(v, [])
            if all([len(components) - 1 == len(adj[v2]) for v2 in components]):
                res += 1
        
        return res