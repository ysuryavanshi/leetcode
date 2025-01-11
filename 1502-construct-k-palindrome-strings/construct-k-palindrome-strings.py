class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False

        count = Counter(s)
        if sum([count[c] % 2 != 0 for c in count]) > k:
            return False

        return True