# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = deque([root])
        ans = []
        
        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.popleft()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            if node:
                ans.append(node.val)
        
        return ans