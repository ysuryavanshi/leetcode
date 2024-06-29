class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)

        ans = deque()
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)