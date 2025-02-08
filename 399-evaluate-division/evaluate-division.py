class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), val in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1/val
        
        for i in graph:
            for j in graph[i]:
                for k in graph[i]:
                    graph[j][k] = 1 if j == k else graph[j][i] * graph[i][k]
        
        return [graph[u].get(v, -1) for u, v in queries]