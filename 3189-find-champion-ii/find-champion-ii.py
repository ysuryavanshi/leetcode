class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = {i: 0 for i in range(n)}
        for _, v in edges:
            in_degree[v] += 1
        
        ans = None
        count = 0
        for key, value in in_degree.items():
            if value == 0:
                if count == 0:
                    ans = key
                    count = 1
                else:
                    return -1
        return ans