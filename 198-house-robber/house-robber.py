class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def helper(i):
            if i >= n:
                return 0
            return max(nums[i] + helper(i + 2), helper(i + 1))
        
        return helper(0)