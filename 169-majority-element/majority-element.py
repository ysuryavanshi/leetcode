class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d: d[n] = 1
            else: d[n] += 1
        
        m, n = None, 0
        for k, v in d.items():
            if v > n: m, n = k, v
        return m
