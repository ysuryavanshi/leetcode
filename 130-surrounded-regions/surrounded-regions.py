class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            visited[r][c] = 1
            directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for dr, dc in directions:
                if 0 <= dr < ROWS and 0 <= dc < COLS and not visited[dr][dc] and board[dr][dc] == 'O':
                    dfs(dr, dc)

        for i in range(ROWS):
            if not visited[i][0] and board[i][0] == 'O':
                dfs(i, 0)
            if not visited[i][COLS-1] and board[i][COLS-1] == 'O':
                dfs(i, COLS-1)
        
        for i in range(COLS):
            if not visited[0][i] and board[0][i] == 'O':
                dfs(0, i)
            if not visited[ROWS-1][i] and board[ROWS-1][i] == 'O':
                dfs(ROWS-1, i)

        for i in range(ROWS):
            for j in range(COLS):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'
