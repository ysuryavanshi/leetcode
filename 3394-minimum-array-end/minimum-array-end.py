class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # res = x
        # i_x = i_n = 1

        # while i_n <= n - 1:
        #     if i_x & x == 0:
        #         if i_n & (n - 1):
        #             res = res | i_x
        #         i_n <<= 1
        #     i_x <<= 1
        # return res


        result = x
        remaining = n - 1
        position = 1

        while remaining:
            if not (x & position):
                result |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
        
        return result