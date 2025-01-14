class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        res = []
        x = defaultdict(int)

        for i in range(len(A)):
            if A[i] not in x:
                x[A[i]] = 1
            else:
                count += 1
            
            if B[i] not in x:
                x[B[i]] = 1
            else:
                count += 1
            res.append(count)
        return res