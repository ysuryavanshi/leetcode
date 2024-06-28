class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        k = 1
        l = r = 0

        for r in range(len((nums))):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r-l