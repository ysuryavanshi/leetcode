class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(number) -> bool:
            if number == 1:
                return False
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
        
        res = []
        prev = None
        for i in range(left, right + 1):
            if not is_prime(i):
                continue
            
            if not prev:
                prev = i
                continue
            
            dif = i - prev

            if dif <= 2:
                return [prev, i]
            
            if not res or dif < res[1] - res[0]:
                res = [prev, i]
            
            prev = i

        return res or [-1, -1]