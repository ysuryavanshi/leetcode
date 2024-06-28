class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        count = [0] * n
        
        for road in roads:
            count[road[0]] += 1 
            count[road[1]] += 1 

        max_imp = 0
        count.sort(reverse=True)
        for c in count:
            max_imp += c * n
            n -= 1
        return max_imp
