class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        f_set = set()

        for f in folder:
            chars = f[1:].split('/')
            cur = ''
            for c in chars:
                cur += '/' + c
                if cur in f_set: break
            else:
                f_set.add(cur)
        return list(f_set)
