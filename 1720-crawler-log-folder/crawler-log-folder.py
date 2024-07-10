class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == '../':
                if ans > 0: ans -= 1
            elif log != './': ans += 1
        return ans
