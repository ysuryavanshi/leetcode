# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        items = []
        for node in lists:
            while node:
                items.append(node.val)
                node = node.next
        
        items.sort()
        dummy = ListNode()
        node = dummy
        for i in items:
            node.next = ListNode(i)
            node = node.next
        
        return dummy.next
            