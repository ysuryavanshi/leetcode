class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5]
        for _ in range(3, n):
            dp.append((dp[-1] * 2 + dp[-3]) % 1000000007)
        return dp[n-1]