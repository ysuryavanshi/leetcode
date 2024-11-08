class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [nums[0]]
        ans = []
        max_k = (2 ** maximumBit - 1)

        for num in nums[1:]:
            prefix_xor.append(prefix_xor[-1] ^ num)

        for cur_xor in prefix_xor[::-1]:
            ans.append(max_k ^ cur_xor)

        return ans