# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head

        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        k = k % len(values)

        if k == 0: return head

        values =  values[len(values)-k:] + values[:len(values)-k]
        root = node = ListNode()
        for value in values:
            new_node = ListNode(value)
            node.next = new_node
            node = node.next
        return root.next