# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = []
        def dfs(node, l):
            if len(res) > l:
                res[l] = max(res[l], node.val)
            else:
                res.append(node.val)
            
            if node.left:
                dfs(node.left, l + 1)
            if node.right:
                dfs(node.right, l + 1)
        dfs(root, 0)
        return res
