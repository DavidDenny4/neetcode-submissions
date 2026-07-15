class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node, parent)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            a, b = edge[0], edge[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        return dfs(0, 0) and len(visited) == n
        

            
