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
        
        mapp = {}
        cur = head
        while cur:
            mapp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mapp[cur].next = mapp.get(cur.next)
            mapp[cur].random = mapp.get(cur.random)
            cur = cur.next
        return mapp[head]
