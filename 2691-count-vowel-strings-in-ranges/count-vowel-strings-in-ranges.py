class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p_count = [0]
        vowels = ('a', 'e', 'i', 'o', 'u')

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                p_count.append(p_count[-1] + 1)
            else:
                p_count.append(p_count[-1])
        
        res = []
        for l, r in queries:
            res.append(p_count[r + 1] - p_count[l])

        return res