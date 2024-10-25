# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        ans = []
        
        while stack:
            ans.append(stack[-1].val)
            n = []
            for node in stack:
                if node.left: n.append(node.left)
                if node.right: n.append(node.right)
            stack = n
        return ans