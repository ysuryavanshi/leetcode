class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = 10 ** 4

        for p in prices:
            res = max(res, p - low)
            low = min(low, p)

        return res