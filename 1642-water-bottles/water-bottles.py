class Solution:
    def foo(self, empty, numExchange):
        if empty < numExchange:
            return 0
        q, r = divmod(empty, numExchange)
        return q + self.foo(q + r, numExchange)
        

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + self.foo(numBottles, numExchange)