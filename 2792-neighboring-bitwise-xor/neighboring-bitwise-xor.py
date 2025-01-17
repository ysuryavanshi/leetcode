class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = last = 0
        for num in derived:
            if num == 1: last = ~last
        
        return False if first != last else True