class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        topo = []

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            
            topo.append(node)
        
        for course in adj:
            dfs(course)
        
        print(f"topo is {topo}")
        return len(topo) == numCourses