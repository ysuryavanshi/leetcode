class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)

        for pre_req, course in prerequisites:
            adj_list[course].append(pre_req)
        
        def dfs(course):
            if course not in pre_req_map:
                pre_req_map[course] = set()
                for pre_req in adj_list[course]:
                    pre_req_map[course] |= dfs(pre_req)
                pre_req_map[course].add(course)
            return pre_req_map[course]

        pre_req_map = {}
        for course in range(numCourses):
            dfs(course)

        res = []
        for prereq, course in queries:
            res.append(prereq in pre_req_map[course])
        
        return res