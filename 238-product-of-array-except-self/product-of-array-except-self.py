class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pp = sp = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pp
            pp *= nums[i]
        
        for i in reversed(range(len(nums))):
            res[i] *= sp
            sp *= nums[i]
        
        return res