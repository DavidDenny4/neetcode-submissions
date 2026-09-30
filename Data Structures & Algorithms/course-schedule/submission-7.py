class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        # already checked
        visited = set()

        def is_cycle(course, visiting):
            if course in visiting:
                return True
            
            visited.add(course)
            for pre_req in adj_list[course]:
                visiting = set()
                visiting.add(pre_req)
                if is_cycle(pre_req, visiting):
                    return True
                visting.remove(pre_req)
            return False

        # each course has list of pre req needed {"0: [1, 2, 3], 1: [4, 5]"}
        for i in range(numCourses):
            adj_list[i] = []

        for req in prerequisites:
            a = req[0]
            b = req[1]
            adj_list[a].append(b)
        
        for course in adj_list:
            if is_cycle(course, visited):
                return False
        return True

