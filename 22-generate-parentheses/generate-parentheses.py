class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_, closed, s):
            if open_ == closed and open_ + closed == n * 2:
                res.append(s)
                return
            
            if open_ < n:
                backtrack(open_ + 1, closed, s + '(')
            
            if closed < open_:
                backtrack(open_, closed + 1, s + ')')
        
        backtrack(0, 0, '')
        return res
            