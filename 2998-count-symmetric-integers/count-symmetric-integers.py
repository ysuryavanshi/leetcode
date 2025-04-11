class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for num in range(low, high + 1):
            num = str(num)
            len_num = len(num)
            if not len(num) % 2:
                if sum([int(i) for i in num[0:len_num//2]]) == sum([int(i) for i in num[len_num//2:]]):
                    res += 1
        
        return res