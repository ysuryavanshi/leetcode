class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        n = len(pref)
        for word in words:
            res += (len(word) >= n) and (word[:n] == pref)
        return res