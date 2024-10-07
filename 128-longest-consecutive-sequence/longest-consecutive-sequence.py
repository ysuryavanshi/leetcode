class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        while nums:
            low = high = nums.pop()

            while low - 1 in nums or high + 1 in nums:
                if low - 1 in nums:
                    nums.remove(low - 1)
                    low -= 1
                if high + 1 in nums:
                    nums.remove(high + 1)
                    high += 1
            
            ans = max(ans, high - low + 1)
        return ans