# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        empty_node = TreeNode(0)
        queue = deque([root, empty_node])

        level_sum = 0
        while queue:
            element = queue.popleft()
            if element == empty_node:
                heapq.heappush(levels, -1 * level_sum)
                level_sum = 0
                if queue:
                    queue.append(empty_node)                
            else:
                level_sum += element.val
                if element.left: queue.append(element.left)
                if element.right: queue.append(element.right)
        
        while k > 1 and levels:
            _ = heapq.heappop(levels)
            k -= 1
        
        return -levels[0] if levels else -1
            
