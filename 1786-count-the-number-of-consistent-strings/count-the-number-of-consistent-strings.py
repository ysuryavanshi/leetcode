class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        words = [set(w) for w in words]
        ans = 0

        for word in words:
            consistent = False
            for c in word:
                if c not in allowed:
                    consistent = False
                    break
                consistent = True
            if consistent: ans += 1
        return ans