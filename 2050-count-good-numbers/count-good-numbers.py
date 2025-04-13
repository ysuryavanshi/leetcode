class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        
        even_count = prime_count = n // 2
        even_count += n % 2

        def power(n, e):
            if e == 0:
                return 1
            
            if e % 2 == 0:
                return power((n * n) % MOD, e // 2)
            else:
                return (n * power((n * n) % MOD, e // 2)) % MOD

        return power(5, even_count) * power(4, prime_count) % MOD