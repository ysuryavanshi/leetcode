class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = ''
        for c in path.split('/'):
            if c and c != '.':
                if c == '..':
                    if stack: _ = stack.pop(-1)
                else:
                    stack.append(c)
        return '/' + '/'.join(stack)