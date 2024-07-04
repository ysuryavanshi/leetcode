class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        c = Counter(senate)
        stack = []
        i = 0
        while c['R'] and c['D']:
            if stack and stack[-1] != senate[i]:
                _ = stack.pop(-1)
                value = senate.pop(i)
                c[value] -= 1
            else:
                stack.append(senate[i])
                i += 1
            if i >= len(senate):
                i = 0
        return 'Radiant' if c['R'] else 'Dire'