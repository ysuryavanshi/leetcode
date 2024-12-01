class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h_set = set()
        for n in arr:
            if n * 2 in h_set or n/2 in h_set:
                return True
            h_set.add(n)
        
        return False