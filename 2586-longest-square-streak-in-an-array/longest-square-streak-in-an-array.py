class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        while nums:
            n = nums.pop()
            cur_len = 1

            m = n
            while (m:=m**2) in nums:
                nums.remove(m)
                cur_len += 1
            
            m = n
            while (m:=sqrt(m)) in nums:
                nums.remove(m)
                cur_len += 1
            
            if ans < cur_len: ans = cur_len
        return -1 if ans == 1 else ans
