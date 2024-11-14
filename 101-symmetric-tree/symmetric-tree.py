# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(left, right):
            if not left and not right:
                return True
            elif not left or not right or left.val != right.val:
                return False
            return bfs(left.left, right.right) and bfs(left.right, right.left)
        
        return bfs(root.left, root.right)