class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for w in strs:
            sorted_w = ''.join(sorted(w))
            mapp[sorted_w].append(w)
        return list(mapp.values())

