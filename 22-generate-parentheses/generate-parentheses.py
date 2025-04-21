class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_, close, p):
            if open_ == close and open_ + close == 2 * n:
                res.append(p)
                return
            
            if open_ < n:
                backtrack(open_ + 1, close, p + '(')
            
            if close < open_:
                backtrack(open_, close + 1, p + ')')
        
        backtrack(0, 0, '')
        return res