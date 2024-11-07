class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(max(candidates).bit_length()):
            count = sum(1 for c in candidates if c & (1 << i))
            ans = max(ans, count)
        return ans