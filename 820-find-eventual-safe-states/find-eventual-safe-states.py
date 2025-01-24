class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        dp = [0] * len(graph)

        def dfs(i):
            if dp[i] == 1 or len(graph[i]) == 0:
                return True
            elif dp[i] == -1 or i in visited:
                return False
            
            visited.add(i)

            for node in graph[i]:
                if not dfs(node):
                    dp[i] = -1
                    return False
            
            dp[i] = 1
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res
