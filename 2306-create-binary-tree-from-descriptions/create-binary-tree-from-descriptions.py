# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]):
        hmap = {}
        plist = {}
        root = None

        for x, y, l in descriptions:
            if x not in hmap:
                hmap[x] = TreeNode(x)
                if x not in plist:
                    root = x
            if y not in hmap:
                hmap[y] = TreeNode(y)
            plist[y] = x

            if l: hmap[x].left = hmap[y]
            else: hmap[x].right = hmap[y]
        
        while root in plist:
            root = plist[root]
        
        return hmap[root]