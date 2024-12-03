class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree_map =   defaultdict(int)
        outdegree_map = defaultdict(int)
        adj_list = defaultdict(list)
        
        for u, v in pairs:
            adj_list[u].append(v)
            outdegree_map[u] += 1
            indegree_map[v] += 1
        
        start_node = None
        for key in outdegree_map.keys():
            if outdegree_map[key] - indegree_map[key] == 1:
                start_node = key
                break
        
        if start_node == None:
            start_node = pairs[0][0]

        path = []
        stack = [start_node]
        while stack:
            val = stack[-1]
            idx = outdegree_map[val]
            if idx == 0:
                path.append(stack.pop())
            else:
                outdegree_map[val] -= 1
                stack.append(adj_list[val][idx - 1])
        return [[path[i], path[i-1]] for i in range(len(path) - 1, 0, -1)]