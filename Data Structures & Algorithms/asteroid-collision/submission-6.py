class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # The stack will hold asteroids that are still alive, collisions are -> against <-
        for a in asteroids:
            alive = True
            while alive and stack and a < 0 and stack[-1] > 0:
                if stack[-1] > -a:
                    alive = False
                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                else:
                    stack.pop()
            if alive:
                stack.append(a)
        return stack