class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        last = 0
        alt = [0]
        for g in gain:
            last = g + alt[-1]
            alt.append(last)
        return max(alt)