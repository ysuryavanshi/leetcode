# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque([root])
        res = []

        while q:
            maxx = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                maxx = maxx if node.val < maxx else node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxx)

        return res
