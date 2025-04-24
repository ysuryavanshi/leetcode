class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        distinct_subarr = defaultdict(int)

        res = left = 0

        for right in range(len(nums)):
            distinct_subarr[nums[right]] += 1

            while len(distinct_subarr) == len(distinct_nums):
                res += len(nums) - right
                distinct_subarr[nums[left]] -= 1

                if distinct_subarr[nums[left]] == 0:
                    del distinct_subarr[nums[left]]

                left += 1

        return res
                