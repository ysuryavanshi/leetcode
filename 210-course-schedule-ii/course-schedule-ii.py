class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        res = []
        q = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
                res.append(i)

        while q:
            node = q.popleft()
            for course in adj_list[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    res.append(course)
                    q.append(course)

        return res if len(res) == numCourses else []