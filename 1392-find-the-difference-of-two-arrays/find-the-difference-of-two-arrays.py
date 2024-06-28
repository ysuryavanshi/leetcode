class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]

        for n in nums1:
            if n not in nums2:
                if n not in answer[0]:
                    answer[0].append(n)
        
        for n in nums2:
            if n not in nums1:
                if n not in answer[1]:
                    answer[1].append(n)

        return answer