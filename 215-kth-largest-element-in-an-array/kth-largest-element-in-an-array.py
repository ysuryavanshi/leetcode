class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        while k > 1:
            _ = heappop(nums)
            k -= 1
        return -heappop(nums)