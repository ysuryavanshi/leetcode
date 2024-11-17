class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        summ, ans = 0, float("inf")

        for i in range(n):
            summ += nums[i]
            if summ >= k:
                ans = min(ans, i + 1)
            
            while q and summ - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])

            while q and summ <= q[-1][1]:
                _ = q.pop()
            q.append((i, summ))

        return ans if ans != float("inf") else -1