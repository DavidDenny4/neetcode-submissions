class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        for a, b in prerequisites:
            adj[a].append(b)
        

        visited = set()
        path = set()
        topo = []

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            topo.append(node)
            return True

        for course in adj:
            if not dfs(course):
                return []
        return topo           