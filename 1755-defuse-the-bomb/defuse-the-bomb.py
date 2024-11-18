class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        tmp = 2 * code
        n = len(code)
        if k == 0:
            return n * [0]
        elif k > 0:
            return [sum(tmp[i+1:i+1+k]) for i in range(n)]
        else:
            return [sum(tmp[n+i+k:n+i]) for i in range(n)]
