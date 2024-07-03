class Solution:
    def minDifference(self, a: list[int]) -> int:
        if len(a) <= 4:
            return 0
        a.sort()
        return min([sub(i,j) for i,j in zip(a[-4:], a[:4])])