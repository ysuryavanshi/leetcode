class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = 10 ** 4

        for price in prices:
            res = max(res, price - low)
            low = min(low, price)
        
        return res