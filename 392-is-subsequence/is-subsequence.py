class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True 
        
        i, l = 0, len(s)
        for c in t:
            if c == s[i]: i += 1
            if i == l: return True
        return False
