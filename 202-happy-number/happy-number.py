class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            summ, temp = 0, n
            while temp > 0:
                digit, temp = temp % 10, temp // 10
                summ += digit ** 2
            n = summ

        return True if n in [1, 7] else False