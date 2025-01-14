class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        res = []

        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            res.append(len(a.intersection(b)))
        return res