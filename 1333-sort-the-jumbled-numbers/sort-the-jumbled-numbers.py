class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = [str(v) for v in mapping]
        mapped = []

        for num in nums:
            val = ''
            for v in str(num):
                val += mapping[int(v)]
            mapped.append(int(val))

        return [y for x, y in sorted(zip(mapped, nums), key=lambda x: x[0])]