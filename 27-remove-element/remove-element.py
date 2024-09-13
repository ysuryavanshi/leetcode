class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        ans = n
        while i < len(nums):
            if nums[i] == val:
                _ = nums.pop(i)
                ans -= 1
            else:
                i += 1
        
        nums.sort()
        return ans