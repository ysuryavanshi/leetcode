class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i] *=  2
                nums[i + 1] = 0

        res = []
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                res.append(nums[i])
        
        return res + [0] * zeros
