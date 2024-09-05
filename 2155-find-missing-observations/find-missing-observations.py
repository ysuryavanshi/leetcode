class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        r = ((n + len(rolls)) * mean) - sum(rolls)

        if r > 6 * n or r < n: return []
        q, r = divmod(r, n)
        return [q + 1] * r + [q] * (n-r)