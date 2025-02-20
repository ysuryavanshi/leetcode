class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet = set(nums)
        string = []

        def backtrack():
            if len(string) == len(nums):
                return ''.join(string) not in numSet
            
            string.append('0')
            if backtrack():
                return True
            _ = string.pop()

            string.append('1')
            if backtrack():
                return True
            _ = string.pop()
            
            return False
        
        backtrack()
        return ''.join(string)
            
