class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(n):
            res += 4 * (0 + i)
        return res