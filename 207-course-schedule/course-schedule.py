class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        res = 0

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res += 1
            for course in adj_list[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)
        
        return res == numCourses



        # adj_list = [[] for _ in range(numCourses)]
        # in_degree = [0] * numCourses
        # ans = []

        # for course, prereq in prerequisites:
        #     adj_list[prereq].append(course)
        #     in_degree[course] += 1
        
        # q = deque()
        # for i in range(numCourses):
        #     if in_degree[i] == 0:
        #         q.append(i)
        
        # while q:
        #     node = q.popleft()
        #     ans.append(node)
        #     for course in adj_list[node]:
        #         in_degree[course] -= 1
        #         if in_degree[course] == 0:
        #             q.append(course)
        
        # return len(ans) == numCourses
