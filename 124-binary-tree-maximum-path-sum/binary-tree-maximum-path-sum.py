# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, result):
            if not root:
                return 0
            
            left = helper(root.left, result)
            right = helper(root.right, result)

            max_s = max(max(left, right) + root.val, root.val)
            max_r = max(max_s, root.val + left + right)
            result[0] = max(max_r, result[0])
            return max_s
        
        ans = [-float('inf')]
        _ = helper(root, ans)
        return ans[0]