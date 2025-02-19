class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack():
            nonlocal n, k
            if len(res) == n:
                k -= 1
                return True if k == 0 else False
            
            for c in 'abc':
                if res and res[-1] == c:
                    continue
                res.append(c)
                if backtrack():
                    return True
                _ = res.pop()
            return None

        backtrack()
        return ''.join(res)