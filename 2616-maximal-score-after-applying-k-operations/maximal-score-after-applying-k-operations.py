class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        ans = 0
        for _ in range(k):
            ans -= nums[0]
            heapreplace(nums, nums[0]//3)
        return ans