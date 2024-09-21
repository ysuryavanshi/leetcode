class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [i for i in range(1, n + 1)]
        nums.sort(key=lambda x: x/10**(len(str(x))-1))
        return nums