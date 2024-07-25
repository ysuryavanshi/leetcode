class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = [str(v) for v in mapping]

        def mapInt(num):
            val = ''
            for v in str(num):
                val += mapping[int(v)]
            return int(val)

        nums.sort(key=mapInt)
        return nums