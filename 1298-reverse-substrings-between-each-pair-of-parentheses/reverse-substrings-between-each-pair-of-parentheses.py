class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c == ')':
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop())
                else:
                    _ = stack.pop()
                stack.extend(ss)
            else:
                stack.append(c)
        return ''.join(stack)