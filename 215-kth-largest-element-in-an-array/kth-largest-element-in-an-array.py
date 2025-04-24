class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num_heap = []

        for n in nums:
            heappush(num_heap, -n)
        
        while k - 1:
            _ = heappop(num_heap)
            k -= 1
        
        return -heappop(num_heap)