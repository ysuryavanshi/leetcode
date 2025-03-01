# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        items = []
        node = head
        while node:
            items.append(node.val)
            node = node.next
        
        items.sort()
        root = ListNode()
        head = root
        for item in items:
            head.next = ListNode(item)
            head = head.next
        
        return root.next