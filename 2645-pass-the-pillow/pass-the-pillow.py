class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        q, r = divmod(time, n-1)
        if (q % 2) == 0: return r + 1
        return n - r