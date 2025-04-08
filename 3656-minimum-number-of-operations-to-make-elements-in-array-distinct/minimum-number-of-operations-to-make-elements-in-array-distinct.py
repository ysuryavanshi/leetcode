class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        vals = set()
        i = len(nums) - 1

        while i >= 0:
            if nums[i] not in vals:
                vals.add(nums[i])
                i -= 1
            else:
                break

        return ceil((i + 1) / 3)