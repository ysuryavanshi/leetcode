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
        if not head: return None

        cur = head
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        old_head = head
        new_head = head.next
        cur_old = old_head
        cur_new = new_head

        while cur_old:
            cur_old.next = cur_old.next.next
            cur_new.next = cur_new.next.next if cur_new.next else None
            cur_old = cur_old.next
            cur_new = cur_new.next
        
        return new_head