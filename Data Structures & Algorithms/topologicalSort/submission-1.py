class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {}
        top_sort = []
        visited = set()
        path = set()

        for i in range(n):
            adj[i] = []
        
        for a, b in edges:
            adj[a].append(b)

        def dfs(node):
            if node in path or node in visited:
                return
            
            path.add(node)
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            path.remove(node)
            top_sort.append(node)
            
        for node in adj:
            dfs(node)
        
        return top_sort.reverse()
        


