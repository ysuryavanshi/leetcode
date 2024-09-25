class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while s[i] == ' ':
            i -= 1
        
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        
        return i - j
