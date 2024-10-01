class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        n, p, z = [], [], []
        for num in nums:
            if num < 0: n.append(num)
            elif num > 0: p.append(num)
            else: z.append(num)
        
        n_set, p_set = set(n), set(p)

        if z:
            for num in p_set:
                if -1 * num in n_set:
                    ans.add((-1 * num, 0, num))
        
        if len(z) > 2: ans.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in p_set:
                    ans.add(tuple(sorted([target, n[i], n[j]])))
        
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in n_set:
                    ans.add(tuple(sorted([target, p[i], p[j]])))

        return ans

