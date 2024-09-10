# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head

        root = head
        while head.next:
            new_node = ListNode(gcd(head.val, head.next.val), head.next)
            head.next, head = new_node, new_node.next
        
        return root