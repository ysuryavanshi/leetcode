class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        stack = []
        for c in s:
            num = m[c]
            if stack and stack[-1] < num:
                num -= stack.pop(-1)
            stack.append(num)
        return sum(stack)