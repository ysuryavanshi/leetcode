# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def walk(self, node, values):
        if node and node.left == None and node.right == None:
            values.append(node.val)
        if node.left:
            self.walk(node.left, values)
        if node.right:
            self.walk(node.right, values)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_values = []
        root2_values = []
        self.walk(root1, root1_values)
        self.walk(root2, root2_values)
        return root1_values == root2_values