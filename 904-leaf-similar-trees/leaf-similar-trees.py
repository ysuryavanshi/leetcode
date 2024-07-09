class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafseq1=[]
        leafseq2=[]
        self.traversal(root1,leafseq1)
        self.traversal(root2,leafseq2)
        return leafseq1==leafseq2

    def traversal (self,root,leafseq):
        if root==None:
            return

        if root.left==None and root.right==None:
            leafseq.append(root.val)
            return

        self.traversal(root.left,leafseq)
        self.traversal(root.right,leafseq)
        return