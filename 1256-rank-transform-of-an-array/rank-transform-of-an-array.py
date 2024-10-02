class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        rank = {e: i + 1 for i, e in enumerate(a)}
        return list(map(rank.get, arr))