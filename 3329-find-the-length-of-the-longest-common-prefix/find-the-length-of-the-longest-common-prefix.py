class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p = set()
        for num in arr1:
            while num:
                p.add(num)
                num //= 10
        
        ans = 0
        for num in arr2:
            while num:
                if num in p:
                    ans = max(ans, len(str(num)))
                    break
                else:
                    num //= 10
        
        return ans