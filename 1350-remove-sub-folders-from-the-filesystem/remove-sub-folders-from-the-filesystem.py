class Trie:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()

        for path in folder:
            node = root
            for c in path.split('/'):
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.end = True

        def backtrack(node, path):
            if node.end:
                return ['/'.join(path)]
            ans = []
            for c in node.children:
                path.append(c)
                ans += backtrack(node.children[c], path)
                path.pop()
            return ans
        return backtrack(root, [])