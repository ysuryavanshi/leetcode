# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        level = s_level = 1
        s = -float('inf')

        while stack:
            c_sum = sum([s.val for s in stack])
            if c_sum > s:
                s, s_level = c_sum, level
            n = []
            for node in stack:
                if node.left: n.append(node.left)
                if node.right: n.append(node.right)
            stack, n = n, []
            level += 1
        return s_level