class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        p = 0
        while n > 1:
            p = (p + k - 1) % n
            if p == n:
                p = 0
                nums.pop(p)
            else:
                nums.pop(p % n)
            n -= 1
        return nums[0]