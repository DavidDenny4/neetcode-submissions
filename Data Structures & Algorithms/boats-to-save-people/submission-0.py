class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        L, R = 0, len(people) - 1
        while L < R:
            if people[L] + people[R] <= limit:
                count += 1
                L += 1
                R -= 1
            else:
                count += 1
                R -= 1
        return count