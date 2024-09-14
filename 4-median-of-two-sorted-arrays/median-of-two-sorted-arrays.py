class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = m1 = m2 = 0

        for _ in range(0, ((m + n) // 2) + 1):
            m2 = m1
            if i < m and j < n:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < m:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        if (n + m) % 2 == 1: return float(m1)
        else: return (float(m1) + float(m2)) / 2.0