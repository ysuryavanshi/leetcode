"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, root):
        if not root:
            return None
        
        all_nodes = {root.val: Node(root.val, [])}
        q = deque([root])

        while q:
            node = q.popleft()
            new_node = all_nodes[node.val]
            
            for nei in node.neighbors:
                if nei.val not in all_nodes:
                    all_nodes[nei.val] = Node(nei.val, [])
                    q.append(nei)
                
                new_node.neighbors.append(all_nodes[nei.val])

        return all_nodes[root.val]
