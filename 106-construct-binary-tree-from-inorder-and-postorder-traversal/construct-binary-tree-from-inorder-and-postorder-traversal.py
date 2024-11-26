# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        if n == 0:
            return None

        val = postorder.pop(-1)
        idx = inorder.index(val)
        
        root_node = TreeNode(val)
        root_node.left = self.buildTree(inorder[:idx], postorder[:idx])
        root_node.right = self.buildTree(inorder[idx+1:], postorder[idx:])

        return root_node
        
        