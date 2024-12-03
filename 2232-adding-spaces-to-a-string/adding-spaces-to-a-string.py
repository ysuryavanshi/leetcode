class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i = j = 0
        m, n = len(s), len(spaces)

        while j < n:
            if i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(s[i])
            i += 1
        
        if i < m:
            res.append(s[i:])

        return ''.join(res)
