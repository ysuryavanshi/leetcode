class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            s = values[node]
            for j in graph[node]:
                if j != parent:
                    s += dfs(j, node)
            nonlocal ans
            ans += s % k == 0
            return s

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans
