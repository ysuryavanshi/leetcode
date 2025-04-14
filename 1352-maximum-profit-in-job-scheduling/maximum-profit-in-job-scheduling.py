class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))

        dp = [0] * n

        def helper(i):
            if i == n:
                return 0
            if dp[i] != 0:
                return dp[i]
            
            next_i = bisect_left(startTime, endTime[i])
            dp[i] = max(helper(i + 1), profit[i] + helper(next_i))

            return dp[i]
        
        return helper(0)