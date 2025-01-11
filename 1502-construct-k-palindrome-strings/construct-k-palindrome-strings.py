class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False

        count = Counter(s)
        if sum([value % 2 != 0 for _, value in count.items()]) > k:
            return False

        return True