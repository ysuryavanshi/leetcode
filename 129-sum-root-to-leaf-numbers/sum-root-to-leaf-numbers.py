# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, cur):
            nonlocal ans

            cur += str(node.val)
            if not node.left and not node.right:
                ans += int(cur)

            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
            
        dfs(root, '0')
        return ans