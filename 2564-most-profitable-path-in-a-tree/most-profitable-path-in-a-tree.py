class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        time_bob = {}
        def dfs(src, prev, time):
            if src == 0:
                time_bob[0] = time
                return True
            
            for nei in adj_list[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    time_bob[src] = time
                    return True

            return False
        
        dfs(bob, -1, 0)

        q = deque([(0, 0, -1, amount[0])]) # start, time, parent, total
        res = -float('inf')
        
        while q:
            node, time, parent, profit = q.popleft()
            time += 1
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                if nei in time_bob:
                    if time > time_bob[nei]:
                        nei_profit = 0
                    elif time == time_bob[nei]:
                        nei_profit = nei_profit // 2
                
                q.append((nei, time, node, profit + nei_profit))
                
                if len(adj_list[nei]) == 1:
                    res = max(res, profit + nei_profit)

        return res