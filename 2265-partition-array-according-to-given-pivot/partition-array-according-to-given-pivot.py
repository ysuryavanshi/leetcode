class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        pivot_count = 0

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                pivot_count += 1
        
        return left + [pivot] * pivot_count + right
