class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = cur_min = cur_max = 0
        prev_bit = -1
        for n in nums:
            cur_bit = n.bit_count()
            if cur_bit != prev_bit:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min = cur_max = n
                prev_bit = cur_bit
            else:
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
        return cur_min >= prev_max