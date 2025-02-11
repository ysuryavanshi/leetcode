class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        len_p = len(part)
        len_s = len(s)

        while len_s >= len_p and part in s:
            idx = s.index(part)
            s = s[0:idx] + s[idx + len_p:]
            len_s -= len_p
        return s
