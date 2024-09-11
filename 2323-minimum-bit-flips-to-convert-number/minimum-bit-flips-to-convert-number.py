class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        ans = 0

        while xor > 0:
            ans += xor & 1
            xor >>= 1
        return ans