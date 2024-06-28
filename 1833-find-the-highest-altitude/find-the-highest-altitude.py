class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]
        max_alt = last = 0
        for g in gain:
            last = g + alt[-1]
            if last > max_alt:
                max_alt = last
            alt.append(last)
        return max_alt