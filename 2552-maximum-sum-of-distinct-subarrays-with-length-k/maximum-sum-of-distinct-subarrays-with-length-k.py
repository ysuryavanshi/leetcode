class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        left = cur_sum = ans = 0

        for right in range(n):
            if nums[right] not in elements:
                cur_sum += nums[right]
                elements.add(nums[right])

                if right - left + 1 == k:
                    if cur_sum > ans:
                        ans = cur_sum
                
                    cur_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
            else:
                while nums[left] != nums[right]:
                    cur_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
                left += 1
        return ans