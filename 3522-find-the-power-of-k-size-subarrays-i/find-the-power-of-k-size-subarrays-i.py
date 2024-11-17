class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        longest_inc = [(1, nums[0])]

        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                last = longest_inc[-1]
                longest_inc.append((last[0] + 1, nums[i]))
            else:
                longest_inc.append((1, nums[i]))
        
        ans = []
        for i in range(k - 1, n):
            if longest_inc[i][0] >= k: ans.append(longest_inc[i][1])
            else: ans.append(-1)
        return ans