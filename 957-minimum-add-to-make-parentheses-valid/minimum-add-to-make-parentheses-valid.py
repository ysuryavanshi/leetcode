class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0

        for b in s:
            if b == '(': right += 1
            else:
                if right: right -= 1
                else: left += 1
        return left + right