class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1, c2 = num1.bit_count(), num2.bit_count()

        if c1 == c2:
            return num1

        i = 0
        temp = num1
        while c1 > c2:
            if temp & (1 << i):
                c1 -= 1
                temp = temp ^ (1 << i)
            i += 1
        
        while c1 < c2:
            if temp & (1 << i) == 0:
                c1 += 1
                temp = temp | (1 << i)
            i += 1

        return temp