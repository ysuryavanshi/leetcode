class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted([[n, h] for n, h in zip(names, heights)], reverse=True, key=lambda h: h[1])]
