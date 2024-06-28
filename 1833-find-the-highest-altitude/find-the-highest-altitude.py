class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]
        max_alt = 0
        for g in gain:
            a = g + alt[-1]
            if a > max_alt:
                max_alt = a

            alt.append(a)
        return max_alt