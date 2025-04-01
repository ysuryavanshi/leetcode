class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def helper(i):
            if i >= n:
                return 0
            
            return max(questions[i][0] + helper(i + 1 + questions[i][1]), helper(i + 1))
        
        return helper(0)