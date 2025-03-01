class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = -float('inf')
        idx = None
        for i, n in enumerate(nums):
            if n > max_num:
                max_num = n
                idx = i
        return idx