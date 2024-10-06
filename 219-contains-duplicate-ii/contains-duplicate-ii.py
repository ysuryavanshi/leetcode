class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_set = {}
        for i in range(len(nums)):
            if nums[i] in n_set and abs(i - n_set[nums[i]]) <= k:
                return True
            n_set[nums[i]] = i
        return False