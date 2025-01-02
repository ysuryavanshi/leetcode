class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p_count = [0]
        vowels = (['a', 'e', 'i', 'o', 'u'])

        cur = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                cur += 1
            p_count.append(cur)
        
        res = []
        for l, r in queries:
            res.append(p_count[r + 1] - p_count[l])

        return res