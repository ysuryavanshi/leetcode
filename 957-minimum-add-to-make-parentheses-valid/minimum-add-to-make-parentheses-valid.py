class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for b in s:
            if stack and stack[-1] == '(' and b == ')':
                _ = stack.pop()
            else:
                stack.append(b)
        return len(stack)