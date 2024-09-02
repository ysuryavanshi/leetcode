class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = k % sum(chalk)
        for i, c in enumerate(chalk):
            total -= c
            if total < 0: return i