class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        res = []
        x = [0] * (len(A) + 1)

        for i in range(len(A)):
            if not x[A[i]]:
                x[A[i]] = 1
            else:
                count += 1
            
            if not x[B[i]]:
                x[B[i]] = 1
            else:
                count += 1
            res.append(count)
        return res