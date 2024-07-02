class UF:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.n -= 1
        return 1

    def is_connected(self):
        return self.n <= 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice, bob = UF(n), UF(n)
        count = 0

        for t, src, dest in edges:
            if t == 3:
                count += (alice.union(src, dest) | bob.union(src, dest))
        for t, src, dest in edges:
            if t == 1:
                count += alice.union(src, dest)
            elif t == 2:
                count += bob.union(src, dest)

        if bob.is_connected() and alice.is_connected():
            return len(edges) - count
        return -1
