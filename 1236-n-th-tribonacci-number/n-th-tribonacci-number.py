class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        for i in range(3, n + 1):
            arr.append(arr[-3] + arr[-2] + arr[-1])
        return arr[n]