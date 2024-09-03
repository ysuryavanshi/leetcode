class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_s = ''
        for c in s:
            numeric_s += str(ord(c) - 96)
        
        while k:
            su = 0
            for d in numeric_s:
                su += int(d)
            numeric_s = str(su)
            k -= 1

        return int(numeric_s)