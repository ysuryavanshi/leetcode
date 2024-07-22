class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s, d = [], []
        def find(n, val, path):
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += 'L'
            elif n.right and find(n.right, val, path):
                path += 'R'
            return path

        find(root, startValue, s)
        find(root, destValue, d)

        while s and d and s[-1] == d[-1]: s.pop(); d.pop()
        return ''.join('U'*len(s)) + ''.join(reversed(d))