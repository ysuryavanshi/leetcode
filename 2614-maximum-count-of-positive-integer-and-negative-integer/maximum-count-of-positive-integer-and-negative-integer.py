class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        total_neg = bisect_left(nums, 0)
        total_pos = len(nums) - bisect_left(nums, 1)

        return max(total_neg, total_pos)
