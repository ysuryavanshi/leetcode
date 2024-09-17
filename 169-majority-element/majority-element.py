class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = c = 0

        for n in nums:
            if count == 0: c = n
            
            if n == c: count += 1
            else: count -= 1
        return c