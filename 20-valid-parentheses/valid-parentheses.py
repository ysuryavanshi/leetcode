class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for b in s:
            if b in ['(', '{', '[']: stack.append(b)
            elif stack and mapp[b] == stack[-1]: _ = stack.pop()
            else: return False
        return not stack

