class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        res = []

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for course in adj_list[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)
        
        if len(res) == numCourses:
            return res
        return []