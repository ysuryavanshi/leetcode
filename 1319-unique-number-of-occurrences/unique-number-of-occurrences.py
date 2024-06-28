class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ = {}
        for e in arr:
            if e not in occ:
                occ[e] = 1
            else:
                occ[e] += 1

        if len(occ) != len(set(occ.values())):
            return False
        return True