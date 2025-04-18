class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for i in range(len(strs)):
            mapp[''.join(sorted(strs[i]))].append(strs[i])
        
        return list(mapp.values())