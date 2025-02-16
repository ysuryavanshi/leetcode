class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = set()

        def backtrack(i):
            if i == size:
                return True
            
            for num in reversed(range(1, n + 1)):
                if num in used:
                    continue
                if num > 1 and (i+num >= size or res[i+num]):
                    continue
                
                used.add(num)
                res[i] = num
                if num != 1:
                    res[i+num] = num
                
                j = i + 1
                while j < size and res[j]:
                    j += 1
                
                if backtrack(j):
                    return True
                
                used.remove(num)
                res[i] = 0
                if num != 1:
                    res[i+num] = 0
            
            return False
        
        backtrack(0)
        return res
