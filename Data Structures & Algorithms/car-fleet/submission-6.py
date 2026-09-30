class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        count = 0
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        for car in range(len(cars)):
            pos, spe = cars[car]
            time = (target - pos) / spe
            if stack and stack[-1] <= time:
                continue
            stack.append(time)
            count += 1
        return count

