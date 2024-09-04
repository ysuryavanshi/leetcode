class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True):
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(minHeap)
        return res
