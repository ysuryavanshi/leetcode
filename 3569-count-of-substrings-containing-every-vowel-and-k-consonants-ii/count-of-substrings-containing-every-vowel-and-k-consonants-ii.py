class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleast_k(k):
            vowels = defaultdict(int)
            non_vowel = res = l = 0

            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowels[word[r]] += 1
                else:
                    non_vowel += 1
                
                while len(vowels) == 5 and non_vowel >= k:
                    res += (len(word) - r)
                    if word[l] in 'aeiou':
                        vowels[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                    l += 1
            return res

        return atleast_k(k) - atleast_k(k + 1)