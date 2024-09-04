class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        res = 0
        total_sum = 0
        heap = []

        merged = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse=True)

        for n2, n1 in merged:
            if len(heap) == k:
                total_sum -= heapq.heappop(heap)
            total_sum += n1
            heapq.heappush(heap, n1)
            
            if len(heap) == k:
                res = max(res, total_sum * n2)
        return res

        res, prefixSum, minHeap = 0, 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True):
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(minHeap)
        return res
