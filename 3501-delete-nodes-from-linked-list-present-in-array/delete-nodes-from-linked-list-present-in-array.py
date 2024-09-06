# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        while head.val in nums:
            head = head.next
        node = head

        while node:
            while node.next and node.next.val in nums:
                node.next = node.next.next
            node = node.next
        
        return head