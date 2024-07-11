class Solution:
    def pathSum(self, root, targetSum) -> int:
        self.total = 0

        def helper(root, curr):
            if not root:
                return
            helper(root.left, curr + root.val)
            helper(root.right, curr + root.val)
            if curr + root.val == targetSum:
                self.total += 1
        
        def dfs(root):
            if not root:
                return
            helper(root, 0)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.total