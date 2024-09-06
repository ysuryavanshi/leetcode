class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        arr = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            arr.append(max(arr[i-2] + nums[i], arr[i-1]))

        return arr[-1]
