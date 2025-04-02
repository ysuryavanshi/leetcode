class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        @cache
        def helper(i):
            if i >= n:
                return 0
            if dp[i] != 0:
                return dp[i]

            dp[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return dp[i]
        
        return helper(0)