class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapify(nums)

        while len(nums) > 1:
            num1 = heappop(nums)
            num2 = heappop(nums)
            if num1 >= k:
                return res
            
            res += 1
            heappush(nums, num1 * 2 + num2)
        
        return res