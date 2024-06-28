class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]
        last = 0
        for g in gain:
            last = g + last
            alt += [last]
        return max(alt)