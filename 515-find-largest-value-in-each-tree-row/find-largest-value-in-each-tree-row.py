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
            if node is None: return None

            if len(res) == l:
                res.append(node.val)
            else:
                res[l] = max(res[l], node.val)
            
            dfs(node.left, l + 1)
            dfs(node.right, l + 1)

        dfs(root, 0)
        return res
