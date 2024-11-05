# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_levels = [0] * (10 ** 5 + 1)
        node_heights = [0] * (10 ** 5 + 1)
        top2_height = [[0]*10**5, [0]*10**5]
        # node_levels = [0] * 10 ** 2
        # node_heights = [0] * 10 ** 2
        # top2_height = [[0]*5, [0]*5]

        def search(node, level):
            if not node:
                return 0
            node_levels[node.val] = level
            height = 1 + max(
                search(node.left, 1 + level),
                search(node.right, 1 + level),
                )
            node_heights[node.val] = height

            if top2_height[0][level] < height:
                top2_height[0][level], top2_height[1][level] = height, top2_height[0][level]
            elif top2_height[1][level] < height:
                top2_height[1][level] = height
            return height

        search(root, 0)
        ans = []
        for query in queries:
            level = node_levels[query]
            height = node_heights[query]
            if top2_height[0][level] == height:
                ans.append(top2_height[1][level] + level - 1)
            else:
                ans.append(top2_height[0][level] + level - 1)
        return ans