# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0

        while i < len(traversal):
            depth = 0

            while i < len(traversal) and traversal[i] == '-':
                i += 1
                depth += 1
            
            num_start = i
            while i < len(traversal) and traversal[i] != '-':
                i += 1
            
            node = TreeNode(int(traversal[num_start:i]))

            while len(stack) > depth:
                _ = stack.pop()
            
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]