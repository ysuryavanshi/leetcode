class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        mapp = defaultdict(list)

        for num in nums:
            summ, temp = 0, num
            while temp:
                summ += temp % 10
                temp //= 10
            mapp[summ].append(num)
        
        res = 0
        for _, val in mapp.items():
            if len(val) > 1:
                res = max(val[0] + val[1], res)
        
        return res or -1