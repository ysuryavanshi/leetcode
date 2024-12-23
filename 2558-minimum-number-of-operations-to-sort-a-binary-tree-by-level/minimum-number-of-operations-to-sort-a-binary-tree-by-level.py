# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def helper(arr):
            swaps = 0
            new_arr = [(val, idx) for idx, val in enumerate(arr)]
            new_arr.sort()
            visited = [False]*len(arr)

            for i in range(len(arr)):
                if visited[i] or new_arr[i][1] == i:
                    continue
                
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = new_arr[x][1]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps
        
        q = deque([root])
        res = 0

        while q:
            res += helper([node.val for node in q])
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
