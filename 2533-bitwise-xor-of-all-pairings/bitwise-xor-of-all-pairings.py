class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len_1, len_2 = len(nums1), len(nums2)

        res = 0
        if len_1 % 2 == 1:
            for num in nums2:
                res ^= num

        if len_2 % 2 == 1:
            for num in nums1:
                res ^= num

        return res
