class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = res = 0
        for idx, val in enumerate(values):
            res = max(res, dp + val - idx)
            dp = max(dp, val + idx)
        return res

# class Solution:
#     def maxScoreSightseeingPair(self, values: List[int]) -> int:
#         n = len(values)
#         dp = [-1] * (n - 1) + [0]

#         def helper(i):
#             if dp[i] != -1:
#                 return dp[i]
#             dp[i] = helper[i+1] - 1
            
            

#         res = 0
#         for i in range(n):
#             res = max(res, helper(i))
#         return res


# [8,1,5,2,6]
# [7,4,4,2,2]
