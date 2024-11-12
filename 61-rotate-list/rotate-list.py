# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head

        element = head
        n = 1
        while element.next:
            element = element.next
            n += 1

        k = k % n
        element.next = head

        temp_node = head
        for _ in range(n - k - 1):
            temp_node = temp_node.next
        
        ans = temp_node.next
        temp_node.next = None

        return ans

