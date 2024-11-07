class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        for _ in range(n):
            for i in range(n - 1):
                if nums[i].bit_count() == nums[i + 1].bit_count() and nums[i + 1] < nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums == sorted(nums)
