class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        p_max = c_min = c_max = p_count = 0
        for n in nums:
            c_count = n.bit_count()
            if p_count == c_count:
                c_min = min(c_min, n)
                c_max = max(c_max, n)
            elif c_min < p_max:
                return False
            else:
                p_max = c_max
                c_min = c_max = n
                p_count = c_count
        return c_min >= p_max