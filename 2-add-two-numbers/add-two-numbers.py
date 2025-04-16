# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        head = root
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            total = total % 10
            
            head.next = ListNode(total)
            head = head.next
            
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            carry = total // 10
            total %= 10

            head.next = ListNode(total)
            head = head.next

            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            carry = total // 10
            total %= 10

            head.next = ListNode(total)
            head = head.next

            l2 = l2.next

        if carry:
            head.next = ListNode(1)
        
        return root.next