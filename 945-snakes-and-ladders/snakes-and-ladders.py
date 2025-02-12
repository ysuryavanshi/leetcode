class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        line = []

        for i, values in enumerate(board):
            if (n - i) % 2 == 1:
                values.reverse()
            line += values
        
        line.append(-1)
        line.reverse()
        n = len(line)
        
        q = deque([(1, 0)])
        visited = {1}
        
        while q:
            spot, moves = q.popleft()

            for roll in range(1, 7):
                new_spot = spot + roll
                if new_spot >= n:
                    continue
                
                if line[new_spot] != -1:
                    new_spot = line[new_spot]

                if new_spot == n - 1: 
                    return moves + 1
                
                if new_spot not in visited:
                    visited.add(new_spot)
                    q.append((new_spot, moves + 1))
        
        return -1
