class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        lsum = 0
        rsum = sum(nums)

        for i, e in enumerate(nums):
            rsum -= e
            if rsum == lsum:
                return i
            lsum += e
        return -1