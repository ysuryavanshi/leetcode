class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1

        chemistry = 0
        check = skill[0] + skill[-1]
        while i < j:
            if check  !=  skill[i] + skill[j]: return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemistry
