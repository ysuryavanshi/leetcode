class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        last = {int(d): i for i, d in enumerate(num)}

        for i, digit in enumerate(num):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int(''.join(num))
        
        return int(''.join(num))