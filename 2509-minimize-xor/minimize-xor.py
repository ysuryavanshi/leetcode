class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1, c2 = num1.bit_count(), num2.bit_count()

        i = 0
        temp = num1
        while c1 != c2:
            if c1 > c2 and temp & (1 << i):
                c1 -= 1
                temp ^= 1 << i
            if c1 < c2 and temp & (1 << i) == 0:
                c1 += 1
                temp |= 1 << i
            i += 1

        return temp