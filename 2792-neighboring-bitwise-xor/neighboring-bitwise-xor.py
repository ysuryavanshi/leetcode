class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        s = 0
        for d in derived:
            s += d
        return s & 1 == 0