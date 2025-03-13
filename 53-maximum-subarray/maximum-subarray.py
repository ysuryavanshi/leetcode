class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for n in nums[1:]:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)
        
        return max_sum