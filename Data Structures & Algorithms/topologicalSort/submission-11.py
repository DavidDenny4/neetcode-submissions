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
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            visited.add(node)
            for neighbor in adj[node]:
                if dfs(neighbor) == False:
                    return False
            path.remove(node)
            top_sort.append(node)
            return True

        for node in adj:
            dfs(node)
        
        top_sort.reverse()
        return top_sort
