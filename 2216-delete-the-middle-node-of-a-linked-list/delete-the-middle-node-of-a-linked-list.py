# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        current_node = head
        while current_node.next:
            current_node = current_node.next
            n += 1

        if n == 1:
            return None
        n = n // 2

        current_node = head
        while n != 1:
            current_node = current_node.next
            n -= 1
        current_node.next = current_node.next.next
        return head
        

        
        