class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3: return s

        stack = [s[0], s[1]]
        for c in s[2:]:
            if set(stack[-2:]) != set(c):
            # if stack[-2] != c or stack[-1] != c:
                stack.append(c)
        return ''.join(stack)
                    