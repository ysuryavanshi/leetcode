class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                _ = stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)