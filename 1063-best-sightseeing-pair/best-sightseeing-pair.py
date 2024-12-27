class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        suffixMax = [0] * n
        suffixMax[n - 1] = values[n - 1] - (n - 1)

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], values[i] - i)

        maxScore = float('-inf')

        for i in range(n - 1):
            maxScore = max(maxScore, values[i] + i + suffixMax[i + 1])

        return maxScore

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
