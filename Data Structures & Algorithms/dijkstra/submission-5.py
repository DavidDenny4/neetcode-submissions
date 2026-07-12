class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        adj = {}
        for node in range(n):
            adj[node] = []
        for s, e, w in edges:
            adj[s].append((e, w))
        
        # stores shortest length from src to each node in graph 
        shortest = {}
        minheap = []
        heapq.heappush(minheap, (0, src))

        while minheap:
            w, n = heapq.heappop(minheap)

            if n in shortest:
                continue
            
            shortest[n] = w
            for neighbor, weight in adj[n]:
                if neighbor not in shortest:
                    heapq.heappush(minheap, (w + weight, neighbor))
            

        for node in adj:
            if node not in shortest:
                shortest[node] = -1
        
        return shortest