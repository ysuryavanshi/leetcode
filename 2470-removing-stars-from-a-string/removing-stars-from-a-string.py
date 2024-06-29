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


with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for s in inputs:
            print('"%s"'%(Solution().removeStars(s)),file=f)
exit(0)