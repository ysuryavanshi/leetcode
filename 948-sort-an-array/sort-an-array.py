class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums) == 1: return
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]

            mergesort(l)
            mergesort(r)

            merge(l, r, nums)
        
        def merge(l, r, nums):
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]: nums[k] = l[i]; i += 1
                else: nums[k] = r[j]; j += 1
                k += 1
            nums[k:] = l[i:] if i < len(l) else r[j:]
        
        mergesort(nums)
        return nums