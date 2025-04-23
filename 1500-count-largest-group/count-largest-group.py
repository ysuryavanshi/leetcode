class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        
        for i in range(1, n + 1):
            i = str(i)
            summ = 0
            for d in i:
                summ += int(d)
            groups[summ] += 1
        
        maxx = max(groups.values())
        return len([1 for key in groups if groups[key] == maxx])