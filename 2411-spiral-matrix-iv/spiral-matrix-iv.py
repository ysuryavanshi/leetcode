# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c_dr = 0

        ans = [[-1 for _ in range(n)] for _ in range(m)]
        i = j = 0

        while head:
            ans[i][j], head = head.val, head.next
            di, dj = i + dr[c_dr][0], j + dr[c_dr][1]
            if di == m or dj == n or ans[di][dj] != -1:
                c_dr = (c_dr + 1) % 4
                di, dj = i + dr[c_dr][0], j + dr[c_dr][1]
            i, j = di, dj
            
        return ans