class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        temp = []
        a_set = set()
        
        res = []
        count = 0

        for a, b in zip(A, B):
            a_set.add(a)

            i = 0
            while i < len(temp):
                if temp[i] in a_set:
                    count += 1
                    _ = temp.pop(i)
                else:
                    i += 1

            if b in a_set:
                count += 1
            else:
                temp.append(b)
            res.append(count)
        
        return res