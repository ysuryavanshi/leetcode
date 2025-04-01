class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        
        def helper(i):
            if i >= n:
                return 0
            if dp[i] != 0:
                return dp[i]
            
            dp[i] = max(questions[i][0] + helper(i + 1 + questions[i][1]), helper(i + 1))
            return dp[i]
        
        return helper(0)