class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash_w_stock = - prices[0]
        cash_wo_stock = 0

        for price in prices[1:]:
            cash_w_stock = max(cash_wo_stock - price, cash_w_stock)
            cash_wo_stock = max(cash_wo_stock, cash_w_stock + price)

        return cash_wo_stock