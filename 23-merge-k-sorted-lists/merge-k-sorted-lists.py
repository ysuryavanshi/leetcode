# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        def helper(left, right):
            if left == right:
                return lists[left]
            
            mid = (left + right) // 2
            l1 = helper(left, mid)
            l2 = helper(mid + 1, right)
            return merge(l1, l2)

        return helper(0, len(lists) - 1)
