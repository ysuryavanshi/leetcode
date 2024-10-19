class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        inverse = False

        while length > 1:
            mid = length // 2
            if k <= mid: length = mid
            elif k > mid + 1:
                inverse = not inverse
                k = 1 + length - k
                length = mid
            else:
                return '1' if not inverse else '0'
        
        return '0' if not inverse else '1'