class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        curr_max = 0
        for h in range(len(height)):
            max_left[h] = curr_max
            curr_max = max(curr_max, height[h])
        
        curr_max = 0
        for h in range(len(height) - 1, -1, -1):
            max_right[h] = curr_max
            curr_max = max(curr_max, height[h])
        
        total = 0
        for i in range(len(height)):
            total += max(min(max_left[i], max_right[i]) - height[i],0)
        
        return total
