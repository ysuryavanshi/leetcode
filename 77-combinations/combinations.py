class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(nums: list, start: int):
            if len(nums) == k:
                res.append(nums.copy())
            else:
                for i in range(start + 1, n + 1):
                    nums.append(i)
                    backtrack(nums, i)
                    _ = nums.pop()
        
        backtrack([], 0)
        return res