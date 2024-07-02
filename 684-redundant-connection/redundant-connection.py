class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find_parent(node):
            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]