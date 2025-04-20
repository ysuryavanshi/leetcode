# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        items = []
        for l in lists:
            while l:
                items.append(l)
                l = l.next
        
        items.sort(key=lambda x: x.val)
        dummy = ListNode()
        head = dummy
        for item in items:
            head.next = item
            head = head.next

        head.next = None
        return dummy.next