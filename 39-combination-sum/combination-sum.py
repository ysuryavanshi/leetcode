class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, combination, remaining):
            if remaining == 0:
                res.append(combination[:])
                return
            if remaining < 0:
                return
            
            for j in range(i, len(candidates)):
                combination.append(candidates[j])
                backtrack(j, combination, remaining-candidates[j])
                _ = combination.pop()
        
        backtrack(0, [], target)

        return res