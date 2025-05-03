class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in nums:
            dist = abs(num - x)
            heapq.heappush(pq, (-dist, -num))
            if len(pq) > k:
                _ = heapq.heappop(pq)
        
        res = [-heapq.heappop(pq)[1] for _ in range(k)]
        res.sort()
        return res