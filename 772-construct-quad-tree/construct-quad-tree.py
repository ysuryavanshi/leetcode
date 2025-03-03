"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(r, c, n):
            if n == 1:
                return Node(grid[r][c], True)

            n //= 2
            top_l = helper(r, c, n)
            top_r = helper(r, c + n, n)
            bot_l = helper(r + n, c, n)
            bot_r = helper(r + n, c + n, n)

            if all(child.isLeaf and child.val == top_l.val for child in [top_l, top_r, bot_l, bot_r]):
                return Node(top_l.val, True)
            
            return Node(None, False, top_l, top_r, bot_l, bot_r)

        return helper(0, 0, len(grid))