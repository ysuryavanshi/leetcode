class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = count = 0
        last = None
        
        for n in nums:
            if last == n:
                if count < 2:
                    nums[i] = n
                    count += 1
                    i += 1
            else:
                nums[i] = n
                last = n
                count = 1
                i += 1
        for j in range(len(nums) - i):
            _ = nums.pop()
        return i + 1