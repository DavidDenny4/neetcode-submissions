class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        
        def is_cycle(course, visited):
            if course in visited:
                return True
            visited.add(course)
            for pre_req in adj_list[course]:
                if is_cycle(pre_req, visited):
                    return True
            return False

        # each course has list of pre req needed {"0: [1, 2, 3], 1: [4, 5]"}
        for i in range(numCourses):
            adj_list[i + 1] = []
            
        for req in prerequisites:
            a = req[0]
            b = req[1]
            adj_list[a].append(b)
        
        for course in adj_list:
            visited = set()
            if is_cycle(course, visited):
                return False
        return True

