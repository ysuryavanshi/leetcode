class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                res += 1
                nums[i] = 1
                nums[i + 1] = 0 if nums[i + 1] else 1
                nums[i + 2] = 0 if nums[i + 2] else 1

        return res if (nums[-1] == 1 and nums[-2] == 1) else -1