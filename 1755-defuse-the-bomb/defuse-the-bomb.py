class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return [0] * n

        if k > 0:
            ans[0] = summ = sum(code[1:k + 1])
            for l in range(1, n):
                r = (l + k) % n
                summ += -code[l] + code[r]
                ans[l] = summ
        else:
            ans[0] = summ = sum(code[-1:k-1:-1])
            for l in range(1, n):
                r = (l - k) % n
                summ += -code[-l] + code[-r]
                ans[-l] = summ
        return ans
        