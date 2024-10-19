class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1: return '0'
        elif k == (2 ** n) - 1: return '1'
        
        s = '0'
        while len(s) < k:
            s += '1' + s.replace('0', '_').replace('1', '0').replace('_', '1')[::-1]

        return s[k-1]
    