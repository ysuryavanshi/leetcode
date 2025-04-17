class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        z = 0
        n, p = [], []

        for num in nums:
            if num == 0:
                z += 1
            elif num < 0:
                n.append(num)
            else:
                p.append(num)

        res = set()

        N, P = set(n), set(p)
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
            
        if z > 2:
            res.add((0, 0, 0))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return list(res)