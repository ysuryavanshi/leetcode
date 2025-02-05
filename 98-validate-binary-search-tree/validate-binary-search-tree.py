# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        
        def helper(node, min_v, max_v):
            if not node:
                return True
            if not min_v < node.val < max_v:
                return False
            
            if node.right and node.left:
                return (
                    node.left.val < node.val < node.right.val and
                    helper(node.left, min_v, node.val) and
                    helper(node.right, node.val, max_v)
                )
            elif node.right:
                return (
                    node.val < node.right.val and
                    helper(node.right, node.val, max_v)
                )
            elif node.left:
                return (
                    node.left.val < node.val and
                    helper(node.left, min_v, node.val)
                )
            else:
                return True

        return helper(node, float('-inf'), float('inf'))