class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []

        for num in nums1:
            heappush(heap, [num + nums2[0], 0])
        
        while k:
            summ, i = heappop(heap)
            res.append([summ - nums2[i], nums2[i]])

            if i + 1 < len(nums2):
                heappush(heap, [summ - nums2[i] + nums2[i + 1], i + 1])

            k -= 1
        
        return res