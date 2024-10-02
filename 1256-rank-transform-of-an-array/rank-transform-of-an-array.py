class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        a = sorted(set(arr))
        for i, e in enumerate(a):
            rank[e] = i + 1
        return list(map(rank.get, arr))