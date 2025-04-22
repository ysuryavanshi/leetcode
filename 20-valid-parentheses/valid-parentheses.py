class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif c not in mapp:
                stack.append(c)
            elif mapp[c] == stack[-1]:
                _ = stack.pop()
            else:
                return False
        
        return not stack
