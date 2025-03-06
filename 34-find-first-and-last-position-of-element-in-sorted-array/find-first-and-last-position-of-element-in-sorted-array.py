class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        left = bisect_left(nums, target)
        right = bisect_left(nums, target + 1)
        return [left, right - 1]