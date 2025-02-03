class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        start, res = 0, 1

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                res = max(res, i - start + 1)
            else:
                start = i
        
        start = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                res = max(res, i - start + 1)
            else:
                start = i

        return res