class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = k % sum(chalk)
        for i in range(len(chalk)):
            total -= chalk[i]
            if total < 0: return i