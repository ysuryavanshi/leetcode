class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]

        nums1.sort()
        nums2.sort()

        for n1 in nums1:
            found = False
            for n2 in nums2:
                if n1 == n2:
                    found = True
                elif n1 < n2:
                    break
            if not found and n1 not in answer[0]:
                answer[0].append(n1)

        for n2 in nums2:
            found = False
            for n1 in nums1:
                if n1 == n2:
                    found = True
                elif n2 < n1:
                    break
            if not found and n2 not in answer[1]:
                answer[1].append(n2)
        return answer