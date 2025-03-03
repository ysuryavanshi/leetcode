class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        i = 0
        pivot_count = 0
        for n in nums:
            if n < pivot:
                res.insert(i, n)
                i += 1
            elif n > pivot:
                res.append(n)
            else:
                pivot_count += 1
        
        for _ in range(pivot_count):
            res.insert(i, pivot)

        return res