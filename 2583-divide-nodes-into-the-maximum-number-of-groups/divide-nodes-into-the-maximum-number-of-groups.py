class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def get_connected_components(source):
            q = deque([source])
            components = set([source])
            while q:
                node = q.popleft()
                for neig in adj[node]:
                    if neig in components:
                        continue
                    q.append(neig)
                    components.add(neig)
            return components
        
        def create_groups(source):
            q = deque([(source, 1)]) # (node, group)
            distance = {source: 1} # distance of a node from source + 1

            while q:
                node, length = q.popleft()
                for neig in adj[node]:
                    if neig in distance:
                        if distance[neig] == length:
                            return -1
                        continue
                    q.append((neig, length + 1))
                    distance[neig] = length + 1
                    visited.add(neig)

            return max(distance.values())

        visited = set()
        res = 0

        for i in range(1, n + 1):
            if i in visited:
                continue
            
            visited.add(i)
            components = get_connected_components(i)

            max_component = 0
            for component in components:
                n_groups = create_groups(component)
                if n_groups == -1:
                    return -1
                max_component = max(n_groups, max_component)
            
            res += max_component

        return res