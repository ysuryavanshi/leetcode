class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def helper(n):
            ans = 0
            if n > high:
                return ans
            if low <= n <= high:
                ans += 1
            
            if n + zero <= high:
                ans += helper(n + zero)
            if n + one <= high:
                ans += helper(n + one)
            
            return ans % (10 ** 9 + 7)
        
        return helper(0)