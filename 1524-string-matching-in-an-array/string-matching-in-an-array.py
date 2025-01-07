class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        c_words = ' '.join(words)
        res = [i for i in words if c_words.count(i) > 1]
        return res