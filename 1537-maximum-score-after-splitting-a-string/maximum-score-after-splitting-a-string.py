class Solution:
    def maxScore(self, s: str) -> int:
        ans = s.count('1')
        res = 0

        for c in s[:-1]:
            ans += 1 if c == '0' else -1
            res = max(ans, res)
        
        return res