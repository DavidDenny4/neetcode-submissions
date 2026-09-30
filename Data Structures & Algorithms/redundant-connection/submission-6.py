class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = {}
        rank = {}

        for i in range(1, len(edges) + 1):
            parent[i] = i
            rank[i] = 1
        
        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(node_a, node_b):
            p_a, p_b = find(a), find(b)
            if p_a == p_b:
                return False
            
            if rank[p_a] < rank[p_b]:
                parent[p_a] = p_b
                rank[p_b] += 1
            else:
                rank[p_b] = p_a
                rank[p_a] += 1
            return True
        
        res = edges[1]
        for edge in edges:
            if union(edge[0], edge[1]) == False:
                res = edge
        return res 