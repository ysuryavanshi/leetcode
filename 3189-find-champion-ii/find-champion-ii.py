class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = {i: 0 for i in range(n)}
        for _, v in edges:
            in_degree[v] += 1
        
        w = [key for key, value in in_degree.items() if value == 0]

        return w[0] if len(w) == 1 else -1
