class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def foo(n, k):
            return 0 if n == 1 else (foo(n - 1, k) + k) % n
    
        return foo(n, k) + 1