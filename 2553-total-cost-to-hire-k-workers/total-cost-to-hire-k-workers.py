class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        heap = []

        ans = p1 = 0
        p2 = len(costs) - 1

        while p1 < candidates:
            heapq.heappush(heap, (costs[p1], p1))
            p1 += 1
        
        while p2 >= len(costs) - candidates and p2 >= p1:
            heapq.heappush(heap, (costs[p2], p2))
            p2 -= 1
        
        for _ in range(k):
            c, i = heapq.heappop(heap)
            ans += c

            if p1 <= p2:
                if i < p1:
                    heapq.heappush(heap, (costs[p1], p1))
                    p1 += 1
                else:
                    heapq.heappush(heap, (costs[p2], p2))
                    p2 -= 1

        return ans