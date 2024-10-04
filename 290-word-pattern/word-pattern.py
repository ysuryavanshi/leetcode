class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = [c for c in pattern]
        s = s.split()

        if len(pattern) != len(s):
            return False

        map1 = {}
        map2 = {}

        for i, j in zip(pattern, s):
            if i not in map1 and j not in map2:
                map1[i] = j
                map2[j] = i
            elif (i in map1 and map1[i] == j) and (j in map2 and map2[j] == i):
                continue
            else:
                return False
        return True