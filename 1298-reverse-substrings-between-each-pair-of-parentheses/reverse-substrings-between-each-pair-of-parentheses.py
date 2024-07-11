class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop(-1))
                else:
                    _ = stack.pop(-1)
                stack.extend(ss)
            else:
                stack.append(c)
        return ''.join(stack)