class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(num, stack, target):
            if len(stack) == k:
                if target == 0:
                    ans.append(stack)
                return
            
            for i in range(num + 1, 10):
                if i <= target:
                    backtrack(i, stack + [i], target - i)
                else: return

        backtrack(0, [], n)
        return ans