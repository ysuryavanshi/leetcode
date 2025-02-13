class Trie:

    def __init__(self):
        self.chars = {}
        

    def insert(self, word: str) -> None:
        chars = self.chars
        for c in word:
            if c not in chars:
                chars[c] = {}
            chars = chars[c]
        chars['*'] = True
        

    def search(self, word: str) -> bool:
        chars = self.chars
        for c in word:
            if c in chars:
                chars = chars[c]
            else:
                return False
        return '*' in chars
        

    def startsWith(self, prefix: str) -> bool:
        chars = self.chars
        for c in prefix:
            if c in chars:
                chars = chars[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)