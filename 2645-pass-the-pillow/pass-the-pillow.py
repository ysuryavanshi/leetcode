class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = 1
        i = 1
        while time:
            i += d
            if i == 1 or i == n:
                d *= -1
            time -= 1
        return i 