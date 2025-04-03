class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = d = high = 0

        for num in nums:
            res = max(res, d * num)
            d = max(d, high - num)
            high = max(high, num)
        
        return res