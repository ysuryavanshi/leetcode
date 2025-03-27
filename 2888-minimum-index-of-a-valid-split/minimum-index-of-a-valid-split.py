class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)

        dom = max(count, key=count.get)
        count_right = count[dom]
        count_left = 0

        for left in range(n - 1):
            if nums[left] == dom:
                count_left += 1
                count_right -= 1
                if count_left / (left + 1) > 0.5 and count_right / (n - (left + 1)) > 0.5:
                    return left

        return -1