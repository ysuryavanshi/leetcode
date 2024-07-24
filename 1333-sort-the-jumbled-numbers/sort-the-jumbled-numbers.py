class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapInt(num):
            digs = [int(c) for c in str(num)]
            n = len(digs)
            m = 0
            for i in range(n):
                m += 10**(n-1-i) * mapping[digs[i]]
            return m
        nums.sort(key=mapInt)
        return nums