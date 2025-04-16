class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            rightX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            leftX = float('inf') if partitionX == m else nums1[partitionX]
            leftY = float('inf') if partitionY == n else nums2[partitionY]
            
            if rightX <= leftY and rightY <= leftX:
                if (m + n) % 2 == 0:
                    return (max(rightX, rightY) + min(leftX, leftY)) / 2
                else:
                    return max(rightX, rightY)
            elif rightX > leftY:
                high = partitionX - 1
            else:
                low = partitionX + 1