# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []

        q = deque([root])

        while q:
            cur_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level_sum.append(cur_sum)

        q.append((root, root.val))
        lvl = 0
        while q:
            for i in range(len(q)):
                node, sibling_sum = q.popleft()
                node.val = level_sum[lvl] - sibling_sum
                if node.left:
                    q.append((node.left, node.left.val + (node.right.val if node.right else 0)))
                if node.right:
                    q.append((node.right, node.right.val + (node.left.val if node.left else 0)))
            lvl += 1
        return root