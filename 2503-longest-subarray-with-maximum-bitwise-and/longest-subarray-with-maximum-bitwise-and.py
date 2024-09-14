class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        c = l = 0
        for num in nums:
            if num == m:
                c += 1
                l = max(l, c)
            else:
                c = 0
        return l