class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        running_sum = nums[0]

        for n in nums[1:]:
            running_sum = max(n, running_sum + n)
            res = max(res, running_sum)
        
        return res
