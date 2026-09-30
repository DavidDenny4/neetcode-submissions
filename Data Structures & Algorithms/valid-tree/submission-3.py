class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for n in adj_list[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            return True
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            a, b = edge[0], edge[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        for node in adj_list:
            print(f"node is {node} and adj list is {adj_list[node]}")
            if adj_list[node] == [] or not dfs(node):
                return False
        return True
        

            
