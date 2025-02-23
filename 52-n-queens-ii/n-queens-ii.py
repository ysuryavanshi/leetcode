class Solution:
    def totalNQueens(self, n: int) -> int:
        visited_cols = set()
        visited_d1 = set()
        visited_d2 = set()

        res = set()
        def backtrack(r) -> int:
            if r == n:
                return 1
            
            count = 0
            for c in range(n):
                if not (c in visited_cols or (r - c) in visited_d1 or (r + c) in visited_d2):

                    visited_cols.add(c)
                    visited_d1.add(r - c)
                    visited_d2.add(r + c)

                    count += backtrack(r + 1)

                    visited_cols.remove(c)
                    visited_d1.remove(r - c)
                    visited_d2.remove(r + c)

            return count
        
        return backtrack(0)