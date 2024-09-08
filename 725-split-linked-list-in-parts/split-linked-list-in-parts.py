class Solution:
    def splitListToParts(self, head, k: int):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        base_size, extra = divmod(length, k)
        ans = []

        for _ in range(k):
            dummy = ListNode()
            part_head = dummy

            for _ in range(base_size + (extra > 0)):
                dummy.next, head, dummy = head, head.next, head

            if extra > 0: extra -= 1

            dummy.next = None
            ans.append(part_head.next)

        return ans