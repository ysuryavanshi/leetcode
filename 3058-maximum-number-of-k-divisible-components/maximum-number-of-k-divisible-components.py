class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        edges.sort()
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = 0
        def dfs(node, parent):
            total = values[node]
            for child in graph[node]:
                if child != parent:
                    total += dfs(child, node)
            if total % k == 0:
                nonlocal res
                res += 1
            return total
        
        dfs(0, -1)

        return res