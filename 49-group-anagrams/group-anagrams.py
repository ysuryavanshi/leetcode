class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for i in range(len(strs)):
            mapp[''.join(sorted(strs[i]))].append(i)
        
        res = []
        for key, value in mapp.items():
            group = []

            for i in value:
                group.append(strs[i])

            res.append(group)

        return res