class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_bitcount = prev_max = cur_max = 0
        
        for num in nums:
            cur_bitcount = num.bit_count()
            if cur_bitcount == prev_bitcount:
                cur_max = max(cur_max, num)
            else:
                prev_max = cur_max
                cur_max = num
                prev_bitcount = cur_bitcount
            if num < prev_max:
                return False
        
        return num >= prev_max