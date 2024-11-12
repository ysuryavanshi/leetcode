# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(), ListNode()
        before_cur, after_cur = before, after

        while head:
            if head.val < x:
                before_cur.next, before_cur = head, head
            else:
                after_cur.next, after_cur = head, head
            head = head.next
        
        after_cur.next = None
        before_cur.next = after.next
        return before.next