class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        box = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    k = (i // 3) * 3 + j // 3
                    if num not in rows[i]: rows[i].add(num)
                    else: return False

                    if num not in cols[j]: cols[j].add(num)
                    else: return False

                    if num not in box[k]: box[k].add(num)
                    else: return False
        return True