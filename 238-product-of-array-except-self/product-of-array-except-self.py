class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp, sp = 1, 1
        result = [0] * n
        for i in range(n):
            result[i] = pp
            pp *= nums[i]
        for i in range(n-1, -1, -1):
            result[i] *= sp
            sp *= nums[i]
        return result