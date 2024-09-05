class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        r = ((n + len(rolls)) * mean) - sum(rolls)

        base_roll, r = divmod(r, n)
        if base_roll <= 0 or base_roll > 6:
            return []
        
        ans = [base_roll] * n
        for i, a in enumerate(ans):
            if a < 6:
                diff = 6 - a
                if r >= diff:
                    ans[i] = 6
                    r -= diff
                else:
                    ans[i] += r
                    r = 0
        
        if r > 0: return []
        return ans