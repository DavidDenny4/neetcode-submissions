class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        def dfs(node):
            if node in visted:
                return
            visited.add(node)
            for n in adj[node]:
                dfs(n)
        
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            a, b = edge[0], edge[1]
            adj[a].append(b)
            adj[b].append(a)
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1
        return count
        