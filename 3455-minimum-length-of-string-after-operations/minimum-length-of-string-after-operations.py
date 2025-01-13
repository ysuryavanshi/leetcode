from string import ascii_lowercase

class Solution:
    def minimumLength(self, s: str) -> int:
        chars = set(ascii_lowercase)
        
        ans = 0
        for c in chars:
            count = s.count(c)
            if count & 1:
                ans += 1
            elif count != 0:
                ans += 2
        return ans