class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pp = sp = 1

        for i in range(len(nums)):
            res.append(pp)
            pp *= nums[i]
        
        for i in reversed(range(len(nums))):
            res[i] *= sp
            sp *= nums[i]
        
        return res