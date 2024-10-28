class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n_set = set(nums)
        
        ans = 0
        for n in nums:
            temp, count = n, 1
            while (temp := temp ** 2) in n_set:
                count += 1
            ans = max(ans, count)
        return ans if ans > 1 else -1