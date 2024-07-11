class Solution:
    def pathSum(self, root, targetSum) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        
        def dfs(root, root_sum):
            if not root:
                return
            root_sum += root.val
            self.total += self.lookup[root_sum]
            self.lookup[root_sum + targetSum] += 1
            dfs(root.left, root_sum)
            dfs(root.right, root_sum)
            self.lookup[root_sum + targetSum] -= 1

        dfs(root, 0)
        return self.total