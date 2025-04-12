class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            res = 0
            for i in range(1, 10):
                if i % k == 0:
                    res += 1
            return res
        
        factorial = [1]
        for i in range(1, n + 1):
            factorial.append(factorial[-1] * i)
        
        seen = set()
        res = 0
        for l in range(10 ** ((n - 1) // 2), 10 ** ((n + 1) // 2)):
            l = str(l)
            r = l[::-1]
            if n % 2 == 1:
                r = r[1:]
            num = l + r

            if int(num) % k != 0:
                continue
            
            s = ''.join(sorted(num))
            if s in seen:
                continue
            seen.add(s)

            count = Counter(num)
            
            total = factorial[-1]
            for key in count.keys():
                total //= factorial[count[key]]
            res += total

            if count['0'] >= 1:
                total = factorial[-2]
                count['0'] -= 1
                for key in count.keys():
                    total //= factorial[count[key]]
                res -= total

        return res