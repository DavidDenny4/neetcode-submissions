class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for rock in asteroids:
            if rock < 0:
                if stack and (stack[-1] * - 1) == rock:
                    stack.pop()
                    continue
                while stack and (-1 * rock) > stack[-1]:
                    stack.pop() 
            else:
                stack.append(rock)

        return stack     