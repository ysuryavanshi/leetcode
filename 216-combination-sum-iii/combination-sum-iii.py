class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        all_c = list(combinations(range(1,10), k))
        ans = [c for c in all_c if sum(c) == n]
        return ans