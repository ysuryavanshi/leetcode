class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        dp = []
        for i in range(n):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            left[i] = len(dp)
        
        dp = []
        for i in range(n - 1, -1, -1):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            right[i] = len(dp)
        
        min_remove = n
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                min_remove = min(min_remove, n - left[i] - right[i] + 1)
        
        return min_remove