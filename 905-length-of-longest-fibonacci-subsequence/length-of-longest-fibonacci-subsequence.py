class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        mapp = set(arr)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                cur = 0
                last = arr[j]
                total = arr[i] + arr[j]
                while total in mapp:
                    cur += 1
                    total, last = total + last, total
                res = max(res, cur)
        return res + 2 if res else 0
