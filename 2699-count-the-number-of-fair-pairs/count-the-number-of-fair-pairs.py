class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        res = 0
        for i in range(len(nums)):
            lower_idx = bisect_left(nums, lower - nums[i], i + 1)
            upper_idx = bisect_left(nums, upper - nums[i] + 1, i + 1)

            res += upper_idx - lower_idx

        return res