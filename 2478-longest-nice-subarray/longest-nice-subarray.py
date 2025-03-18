class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        cur = left = 0

        for right in range(len(nums)):
            while cur & nums[right]:
                cur ^= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
            cur |= nums[right]
            
        return res
