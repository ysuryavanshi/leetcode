# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next: return head
        odd, even = head, head.next
        current = head.next.next
        even.next = None
        n = 3
        while current != None:
            if n % 2 == 0:
                temp = current
                current = current.next 
                temp.next = None
                even.next = temp
                even = even.next
            else:
                temp = current
                current = current.next

                temp.next = odd.next
                odd.next = temp
                odd = odd.next
            n += 1
        return head