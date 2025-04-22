class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(i, total, c_list):
            if total == target:
                res.append(c_list[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > target - total:
                    break
                c_list.append(candidates[j])
                backtrack(j + 1, total + candidates[j], c_list)
                _ = c_list.pop()
        
        backtrack(0, 0, [])
        return res