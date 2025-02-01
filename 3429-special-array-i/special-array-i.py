class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = None
        for i in nums:
            if last == (last:=i & 1):
                return False
        return True