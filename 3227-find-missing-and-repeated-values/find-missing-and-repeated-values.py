class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0, 0]
        h_set = set()

        for i in range(n):
            for j in range(n):
                if (num:=grid[i][j]) in h_set:
                    res[0] = num
                else:
                    h_set.add(num)
        
        for i in range(1, (n * n) + 1):
            if i not in h_set:
                res[1] = i
                break
        
        return res