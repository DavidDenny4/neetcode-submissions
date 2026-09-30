class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        visited = set()
        visiting = set()

        def is_cycle(course):
            if course in visiting:
                return True
            if course in visited:
                return False
            visiting.add(course)
            for pre_req in adj_list[course]:
                visiting.add(pre_req)
                if is_cycle(pre_req):
                    return True
                visiting.remove(pre_req)
            visited.add(course)
            return False

        # each course has list of pre req needed {"0: [1, 2, 3], 1: [4, 5]"}
        for i in range(numCourses):
            adj_list[i] = []

        for req in prerequisites:
            a = req[0]
            b = req[1]
            adj_list[a].append(b)
        
        for course in adj_list:
            if is_cycle(course):
                return False
        return True

