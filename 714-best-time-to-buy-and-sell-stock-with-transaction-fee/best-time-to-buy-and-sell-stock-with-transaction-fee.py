class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        c_ws, c_wos = -prices[0], 0

        for i in range(1, len(prices)):
            c_ws = max(c_ws, c_wos - prices[i])
            c_wos = max(c_wos, c_ws + prices[i] - fee)
        return c_wos
