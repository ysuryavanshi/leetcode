class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        p_sum = [0]

        cur = 0
        for n in nums:
            cur += n
            p_sum.append(cur)
        
        res = 0
        for n in p_sum[1:-1]:
            if n >= cur - n:
                res += 1
        return res
