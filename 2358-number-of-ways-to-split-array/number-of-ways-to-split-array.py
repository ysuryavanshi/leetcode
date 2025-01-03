class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        p_sum = [0]
        s_sum = [0]

        cur = 0
        for n in nums:
            cur += n
            p_sum.append(cur)
        
        cur = 0
        for n in reversed(nums):
            cur += n
            s_sum.insert(0, cur)
        
        res = 0
        for x, y in zip(p_sum[1:-1], s_sum[1:-1]):
            if x >= y: res += 1
        
        return res