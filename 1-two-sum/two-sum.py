class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i, number in enumerate(nums):
            if number in mapp:
                return [i, mapp[number]]
            else:
                remaining = target - number
                mapp[remaining] = i
        return None