class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        
        ans = 0
        def dfs(i, cur_or):
            nonlocal max_or, ans
            if i == len(nums):
                if cur_or == max_or: ans += 1
                return
            
            dfs(i + 1, cur_or)
            dfs(i + 1, cur_or | nums[i])

        dfs(0, 0)
        return ans