class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        print(f"edges is {edges}")
        adj = defaultdict(list)
        for s, e, w in edges:
            adj[s].append((e, w))
        
        print(f"adj is {adj}")
        return {}

     
        