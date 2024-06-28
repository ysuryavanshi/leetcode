class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        cw1 = Counter(word1)
        cw2 = Counter(word2)
        return len(set(cw1) ^ set(cw2)) == 0 and sorted(cw1.values()) == sorted(cw2.values())