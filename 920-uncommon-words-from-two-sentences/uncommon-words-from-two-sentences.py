class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for s in s1.split():
            if s not in d: d[s] = 1
            else: d[s] += 1
        for s in s2.split():
            if s not in d: d[s] = 1
            else: d[s] += 1
        return [k for k, v in d.items() if v == 1]