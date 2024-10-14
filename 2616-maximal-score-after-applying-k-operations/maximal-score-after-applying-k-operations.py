class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [n * -1 for n in nums]
        heapify(nums)
        ans = 0
        while k:
            n = heapq.heappop(nums)
            ans += n
            if n == 1:
                ans += k
                break
            heapq.heappush(nums, floor(n/3))
            k -= 1
        return - 1 * ans