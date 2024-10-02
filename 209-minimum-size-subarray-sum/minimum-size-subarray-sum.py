class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                ans = min(ans, i - left + 1)
                total -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0