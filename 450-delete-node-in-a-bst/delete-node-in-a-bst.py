class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        def successor(root):
            root = root.right
            while root.left: root = root.left
            return root.val

        def predecessor(root):
            root = root.left
            while root.right: root = root.right
            return root.val

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root