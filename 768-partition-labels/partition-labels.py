class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        res = []
        cur_chars = set()
        total = 0

        for i, c in enumerate(s):
            cur_chars.add(c)
            count[c] -= 1
            if count[c] == 0:
                cur_chars.remove(c)
                if not cur_chars:
                    res.append(i - total + 1)
                    total += (i - total + 1)
        return res
