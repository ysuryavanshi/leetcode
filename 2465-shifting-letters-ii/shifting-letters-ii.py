class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)

        for start, end, direction in shifts:
            shift[start] += (1 if direction else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if direction else -1)

        cur = 0
        s = list(s)
        for i in range(n):
            cur += shift[i]
            net = (cur % 26) % 26
            s[i] = chr((ord(s[i]) - 97 + net) % 26 + 97)
        
        return ''.join(s)