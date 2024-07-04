# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        last = None

        while head:
            nxt, head.next = head.next, last
            last, head = head, nxt
        return last
