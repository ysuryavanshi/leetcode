# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        last = None
        ptr = head
        n = 0

        while ptr:
            node = ListNode(ptr.val, last)
            last = node
            ptr = ptr.next
            n += 1

        ans = 0
        i = 0
        while i <= n / 2:
            ans = max(ans, head.val + last.val)
            i += 1
            head = head.next
            last = last.next
        return ans