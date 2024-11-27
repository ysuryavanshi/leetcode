# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.pointer = -1
        self.size = 0
        self.calculate_inorder(root)
    
    def calculate_inorder(self, node):
        if not node: return
        self.calculate_inorder(node.left)
        self.inorder.append(node.val)
        self.size += 1
        self.calculate_inorder(node.right)        

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < self.size - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()