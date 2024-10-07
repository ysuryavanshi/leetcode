class Solution:
    def minLength(self, s: str) -> int:
        sub_string = ''
        for c in s:
            sub_string += c
            while sub_string[-2:] in ['AB', 'CD']:
                sub_string = sub_string[:-2]
        return len(sub_string)