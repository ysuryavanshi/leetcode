"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h_set = {}
        
        node = head
        while node:
            h_set[node] = Node(node.val)
            node = node.next
        
        node = head
        root = dummy = Node(0)
        while node:
            temp = h_set[node]
            dummy.next = temp

            temp.next = h_set[node.next] if node.next else None
            temp.random = h_set[node.random] if node.random else None

            dummy = dummy.next
            node = node.next
        
        return root.next