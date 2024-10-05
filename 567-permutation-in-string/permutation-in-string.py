class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        n = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:n])
        if c1 == c2: return True

        for i in range(1, len(s2) - n + 1):
            c2.subtract(s2[i-1])
            if c2[s2[i-1]] == 0: c2.pop(s2[i-1])

            if s2[i + n - 1] in c2:
                c2[s2[i + n - 1]] += 1
            else: c2[s2[i + n - 1]] = 1
            if c1 == c2:
                return True
        return False