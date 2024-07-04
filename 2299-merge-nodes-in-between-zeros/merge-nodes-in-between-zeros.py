# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        edit_node = head
        current_node = head.next
        total = 0
        while current_node.next != None:
            if current_node.val != 0:
                total += current_node.val
            else:
                edit_node.val = total
                total = 0
                edit_node = edit_node.next
            current_node = current_node.next
        edit_node.val = total
        edit_node.next = None
        return head
