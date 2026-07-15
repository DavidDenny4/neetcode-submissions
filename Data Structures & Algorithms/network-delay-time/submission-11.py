class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create adj list
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))
        
        minHeap = []
        dist = {}
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            dst, node = heapq.heappop(minHeap)
            if node in dist:
                continue
            dist[node] = dst
            for ti, vi in adj[node]:
                if vi not in dist:
                    heapq.heappush(minHeap,(dst + ti, vi))
        
        for i in range(1, n + 1):
            if i not in dist:
                return -1
        return max(dist.values)
