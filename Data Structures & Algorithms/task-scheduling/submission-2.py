class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_map = Counter(tasks)
        max_heap = [-count for count in task_map.values()]
        heapq.heapify(max_heap)
        idle = deque()
        total_time = 0

        while max_heap or idle:
            total_time += 1

            if idle and idle[0][0] == total_time:
                heapq.heappush(max_heap, idle.popleft()[1])

            task = heapq.heappop(max_heap) 
            if task < 0:
                idle.append((total_time + n, task))
        
        return total_time

        
        
