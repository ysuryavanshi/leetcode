class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while right - left >= k:
            if x - nums[left] > nums[right] - x:
                left += 1
            else:
                right -= 1
        
        return nums[left:left + k]