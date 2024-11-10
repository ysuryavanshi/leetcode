# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = defaultdict(int)
        node = head
        while node:
            c[node.val] += 1
            node = node.next
        
        new_head = ListNode()
        node = new_head
        for key in sorted(c):
            if c[key] == 1:
                node.next = ListNode(key)
                node = node.next

        return new_head.next