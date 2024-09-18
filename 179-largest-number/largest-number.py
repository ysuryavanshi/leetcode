class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            return -1 if x + y > y + x else 1
    
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(cmp))
        largest_num = ''.join(nums)
        return '0' if largest_num[0] == '0' else largest_num