class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]
        for g in gain:
            alt.append(g + alt[-1])
        return max(alt)