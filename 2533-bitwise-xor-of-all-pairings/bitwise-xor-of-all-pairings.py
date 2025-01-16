class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) & 1:
            for num in nums2:
                res ^= num

        if len(nums2) & 1:
            for num in nums1:
                res ^= num

        return res
