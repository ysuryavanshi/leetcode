class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join([str(ord(i) - 96) for i in s])
        while k:
            su = 0
            for i in s:
                su += int(i)
            s = str(su)
            k -= 1
        return int(s)