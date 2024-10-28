class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n_dict = {}
        for n in nums:
            n_dict[n] = n * n
        
        ans = 0
        for n in nums:
            if n in n_dict:
                temp, count = n_dict[n], 1
                while temp in n_dict:
                    count += 1
                    temp = n_dict[temp]
                    ans = max(ans, count)
        return ans if ans > 1 else -1