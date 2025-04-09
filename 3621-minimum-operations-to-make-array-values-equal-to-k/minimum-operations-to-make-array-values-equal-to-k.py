class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        vals = set()

        for num in nums:
            if num < k:
                return -1
            
            if num > k and num not in vals:
                res += 1
                vals.add(num)

        return res