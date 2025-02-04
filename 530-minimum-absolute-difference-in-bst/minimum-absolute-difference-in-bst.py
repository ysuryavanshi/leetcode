# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        node_val_list = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            node_val_list.append(node.val)
            dfs(node.right)

        dfs(root)
        return min([node_val_list[i] - node_val_list[i-1] for i in range(1, len(node_val_list))])
