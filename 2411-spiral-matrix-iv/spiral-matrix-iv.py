# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        ans = [[-1]*n for _ in range(m)]
        
        top_row, bottom_row, left_col, right_col = 0, m - 1, 0, n - 1

        while head:
            for j in range(left_col, right_col + 1):
                if head:
                    ans[top_row][j] = head.val
                    head = head.next
            top_row += 1

            for i in range(top_row, bottom_row + 1):
                if head:
                    ans[i][right_col] = head.val
                    head = head.next
            right_col -= 1

            for j in range(right_col, left_col - 1, -1):
                if head:
                    ans[bottom_row][j] = head.val
                    head = head.next
            bottom_row -= 1

            for i in range(bottom_row, top_row - 1, -1):
                if head:
                    ans[i][left_col] = head.val
                    head = head.next
            left_col += 1
        
        return ans