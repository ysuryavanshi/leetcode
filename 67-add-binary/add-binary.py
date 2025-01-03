class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        i = len(a) - 1
        j = len(b) - 1

        res = []
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += a[i]
                i -= 1
            if j >= 0:
                carry += b[j]
                j -= 1

            if carry == 3:
                res.append('1')
                carry = 1
            elif carry == 2:
                res.append('0')
                carry = 1
            elif carry == 1:
                res.append('1')
                carry = 0
            else:
                res.append('0')
        
        if carry:
            res.append('1')
        return ''.join(reversed(res))
