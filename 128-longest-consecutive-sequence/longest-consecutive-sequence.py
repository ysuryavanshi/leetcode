class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_length = 0

        while hset:
            low = high = hset.pop()
            
            while low - 1 in hset or high + 1 in hset:
                if low - 1 in hset:
                    hset.remove(low - 1)
                    low -= 1
                
                if high + 1 in hset:
                    hset.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length