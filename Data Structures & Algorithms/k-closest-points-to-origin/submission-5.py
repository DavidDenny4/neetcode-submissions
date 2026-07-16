class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = (((x - 0) ** 2) + ((y - 0) ** 2)) ** 0.5
            print(f"dist {dist} for {x}, {y}")
            heapq.heappush(min_heap, (-1 * dist, [x, y]))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        print(f"min heap is {min_heap}")
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res