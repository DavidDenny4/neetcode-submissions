class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        L = 0
        max_area = 0
        stack = []
        for R in range(len(heights)):
            start = R
            while stack and stack[-1][1] > heights[R]:
                index, h = stack.pop()
                max_area = max(max_area, (R - index) * h)
                start = index
            stack.push((start, heights[R]))

        while stack:
            index, h = stack.pop()
            max_area = max(max_area, (len(heights) - index) * h)
        
        return max_area
