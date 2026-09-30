class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [count for count in Counter(tasks).values()]
        heapq.heapify(task_count)
        idle_queue = deque() # (time, task_count)
        time = 0

        while task_count or idle_queue:
            
            if idle_queue and idle_queue[0][0] == time:
                heapq.heappush(task_count, idle_queue.popleft()[1])
            
            idle_queue.append((time + n, heaq.heappop(task_count) - 1))

            time += 1
        
        return time
            


        