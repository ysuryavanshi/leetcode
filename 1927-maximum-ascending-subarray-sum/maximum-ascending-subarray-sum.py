class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = cur = last = 0
        for n in nums:
            if n <= last:
                last = cur = n
            else:
                last = n
                cur += n
            res = max(res, cur)
        return res