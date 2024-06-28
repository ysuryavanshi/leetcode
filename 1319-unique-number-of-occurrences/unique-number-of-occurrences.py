class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ = collections.Counter(arr)
        return len(occ) == len(set(occ.values()))