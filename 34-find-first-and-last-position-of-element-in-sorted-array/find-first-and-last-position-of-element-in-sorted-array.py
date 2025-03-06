class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target) # O(logn)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect_left(nums, target + 1)  # O(logn)
        return [left, right - 1]