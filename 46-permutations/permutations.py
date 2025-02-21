class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        res = []

        def backtrack(i, p):
            if len(p) == n:
                res.append(p.copy())
                return
            
            for j in range(0, n):
                if j in visited:
                    continue
                p.append(nums[j])
                visited.add(j)
                backtrack(j + 1, p)
                _ = p.pop()
                visited.remove(j)
        
        backtrack(0, [])
        return res