class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, word_idx):
            if word_idx == len(word):
                return True
            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visited:
                return False
            
            if board[row][col] == word[word_idx]:
                visited.add((row, col))

                for dx, dy in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    if backtrack(dx, dy, word_idx + 1):
                        return True
                visited.remove((row, col))

            return False            
            
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        
        return False