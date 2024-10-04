class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        check = skill[0] + skill[-1]

        for i in range(len(skill) // 2):
            if check  !=  skill[i] + skill[-i - 1]: return -1
            chemistry += skill[i] * skill[-i - 1]
        return chemistry
