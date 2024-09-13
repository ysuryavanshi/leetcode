class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i, num in enumerate(nums2):
            while j < m + i and num >= nums1[j]:
                j += 1
            nums1.insert(j, num)
            j += 1
        for _ in range(n):
            _ = nums1.pop()
