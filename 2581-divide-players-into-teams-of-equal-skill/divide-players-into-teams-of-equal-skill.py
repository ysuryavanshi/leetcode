class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1

        chemistry = 0
        while i < j:
            if skill[0] + skill[-1] !=  skill[i] + skill[j]: return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemistry
