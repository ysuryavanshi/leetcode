class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)

        ans = []
        for i in s:
            if i == '*':
                ans.pop(-1)
            else:
                ans.append(i)
        return ''.join(ans)