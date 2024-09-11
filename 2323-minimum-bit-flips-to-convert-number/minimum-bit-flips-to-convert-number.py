class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while start > 0 or goal > 0:
            s = start & 1
            g = goal & 1

            if s != g:
                flips += 1
            
            start >>= 1
            goal >>= 1
        return flips