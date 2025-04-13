class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_set = {}
        
        for i in range(len(nums)):
            if nums[i] in h_set:
                return [h_set[nums[i]], i]
            else:
                h_set[target - nums[i]] = i