class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                
                left, right = j + 1, len(nums) - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return ans