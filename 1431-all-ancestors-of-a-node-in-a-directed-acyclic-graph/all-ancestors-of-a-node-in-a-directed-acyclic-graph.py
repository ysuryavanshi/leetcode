class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        direct_child = defaultdict(list)
        ans = [[] for _ in range(n)]

        for x, y in edges:
            direct_child[x].append(y)
        
        def dfs(x, curr):
            for child in direct_child[curr]:
                if ans[child] and ans[child][-1] == x:
                    continue
                ans[child].append(x)
                dfs(x, child)

        for edge in range(n):
            dfs(edge, edge)
        return ans