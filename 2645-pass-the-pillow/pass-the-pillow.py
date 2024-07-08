class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = i = 1
        while time:
            time -= 1
            i += d
            if i == 1 or i == n: d *= -1
        return i