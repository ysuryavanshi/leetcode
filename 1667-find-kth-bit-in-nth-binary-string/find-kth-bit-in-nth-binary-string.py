class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        
        def helper(length, k):
            if length == 1: return '0'

            mid = length // 2
            if k <= mid:
                return helper(mid, k)
            elif k > mid + 1:
                ans = helper(mid, 1 + length - k)
                return '0' if ans == '1' else '1'
            else:
                return '1'
        
        return helper(length, k)