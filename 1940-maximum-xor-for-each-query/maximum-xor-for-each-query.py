class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = 2 ** maximumBit - 1

        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]

        for i in range(len(nums)):
            nums[i] ^= n

        return nums[::-1]