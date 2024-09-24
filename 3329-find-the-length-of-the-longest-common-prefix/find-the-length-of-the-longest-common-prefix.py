class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    

class Trie:
    def __init__(self, numbers: str):
        self.root = TrieNode()
        for num in numbers:
            cur = self.root
            for d in num:
                if d not in cur.children:
                    cur.children[d] = TrieNode()
                cur = cur.children[d]
            cur.word = True


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2) < len(arr1):
            arr1, arr2 = arr2, arr1

        arr1 = [str(i) for i in arr1]
        arr2 = [str(i) for i in arr2]

        trie_arr1 = Trie(arr1).root

        ans = 0
        for num in arr2:
            m = 0
            cur = trie_arr1
            for d in num:
                if d in cur.children:
                    m += 1
                    cur = cur.children[d]
                else:
                    break
            ans = max(ans, m)
        return ans