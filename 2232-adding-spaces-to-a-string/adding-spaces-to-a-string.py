class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        stack = []
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                stack.append(' ')
                j += 1
            stack.append(c)
        return ''.join(stack)
